# import pytest
#
# @pytest.fixture
# def db_connection():
#     conn = create_db_connection()
#     yield conn
#     conn.close()
#
# def test_db_query(db_connection):
#     assert db_connection.query('SELECT 1').fetchone() == (1,) is not None

class WeatherAPI:
    def __init__(self):
        self.api_key = config.WEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5"

    async def get_current_weather(self, city: str) -> None:
        """Get current information about weather in the city.
        Args:
            city(str): name of the city
        Returns:
            dict or none: if city is found return dict with data
        Raises:
            Exception: if data not found raise exception
        """
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return self._parse_weather_data(data)
                    else:
                        error_data = await response.json()
                        logger.error(f"Error getting weather data: {error_data}")
                        return None
            except Exception as e:
                logger.error(f"Error getting weather data: {e}")
                return None

    async def get_forecast(self, city: str, days: int = 3) -> dict | None:
        """Fetches weather forecast data for a specified city.

        Args:
            city (str): The name of the city (e.g., "Moscow").
            days (int, optional): Number of forecast days (1-5). Defaults to 3.

        Returns:
            dict | None: A dictionary with daily forecast data.
            Example:
            {
                "2023-10-20": {"max_temp": 18, "min_temp": 12},
                "2023-10-21": {"max_temp": 17, "min_temp": 10}
            }

        Raises:
            aiohttp.ClientResponseError: If the API returns 4xx/5xx status.
            ValueError: If `days` is invalid or city not found.
        """
        if days < 1 or days > 5:
            raise ValueError("Days must be between 1 and 5")

        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "cnt": days * 8,  # 8 точек данных в день (каждые 3 часа)
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, params=params) as response:
                    response.raise_for_status()  # Проверяет 4xx/5xx
                    data = await response.json()
                    return self._parse_forecast_data(data)
            except aiohttp.ClientResponseError as e:
                if e.status == 404:
                    raise ValueError(f"City '{city}' not found") from e
                logger.error(f"HTTP error: {e.status}")
                raise
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                return None




