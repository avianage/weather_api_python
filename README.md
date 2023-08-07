# Weather Forecast API using Python

## Introduction

This is a simple Python-based Weather Forecast API that provides weather information for a specific location using third-party APIs. It is designed to be easy to use and can be integrated into various applications that require weather data.

## Getting Started

To use the Weather Forecast API, follow the steps below:

1. Clone or download the repository to your local machine.
2. Install the required dependencies by running `pip install requests` in the terminal.
3. Obtain API keys from the weather service providers you wish to use. This API currently supports OpenWeatherMap and WeatherAPI.
4. Replace the placeholder API keys in the code with your actual API keys.
5. Run the Python script to get weather information for your desired location.

## Usage

The API offers the following features:

- Get the current weather information for a specific location.
- Get the weather forecast for the next 7 days for a specific location.

### Example

```python
from weather_api import WeatherAPI

# Initialize the WeatherAPI class with your API key
api_key = "your_api_key"
weather_api = WeatherAPI(api_key)

# Get the current weather for a specific location
current_weather = weather_api.get_current_weather(city="New York")

# Get the weather forecast for the next 7 days for a specific location
forecast = weather_api.get_weather_forecast(city="Los Angeles")
```

## API Documentation

### `get_current_weather(city: str) -> dict`

This method returns the current weather information for the specified city.

- Parameters:
  - `city` (str): The name of the city for which you want to retrieve the current weather.

- Returns:
  - `dict`: A dictionary containing the following weather information:
    - `temperature` (float): The current temperature in Celsius.
    - `description` (str): A brief description of the weather (e.g., "cloudy," "sunny").
    - `humidity` (float): The humidity percentage.
    - `wind_speed` (float): The wind speed in km/h.

### `get_weather_forecast(city: str) -> dict`

This method returns the weather forecast for the next 7 days for the specified city.

- Parameters:
  - `city` (str): The name of the city for which you want to retrieve the weather forecast.

- Returns:
  - `dict`: A dictionary containing a list of daily weather forecasts. Each element in the list includes the following information:
    - `date` (str): The date of the forecast (YYYY-MM-DD format).
    - `temperature` (dict): A dictionary containing `min` and `max` temperatures for the day in Celsius.
    - `description` (str): A brief description of the weather (e.g., "cloudy," "sunny").
    - `humidity` (float): The humidity percentage.
    - `wind_speed` (float): The wind speed in km/h.

## Credits

This Weather Forecast API is powered by data from OpenWeatherMap and WeatherAPI. Special thanks to their services for providing free access to weather data.

## License

This project is licensed under the MIT License. You can find the license details in the `LICENSE` file.

## Support and Contribution

If you encounter any issues or have suggestions for improvement, please feel free to raise an issue or submit a pull request. Your contributions are greatly appreciated.

---

**Note:** Ensure to replace `"your_api_key"` in the example code with your actual API keys from the respective weather service providers. Additionally, you may customize and expand this API based on your specific requirements.