using System;
using System.Net.Http;
using System.Text.Json;
using System.Globalization;

using HttpClient client = new HttpClient();

string url = "https://power.larc.nasa.gov/api/temporal/daily/point" +
    "?parameters=T2M,PRECTOTCORR" +
    "&community=AG" +
    "&latitude=13.62" +
    "&longitude=123.18" +
    "&start=20240107" +
    "&end=20240115" +
    "&format=JSON";

try
{
    string response = await client.GetStringAsync(url);
    using JsonDocument document = JsonDocument.Parse(response);

    JsonElement parameters = document.RootElement.GetProperty("properties").GetProperty("parameter");

    JsonElement temperatures = parameters.GetProperty("T2M");   
    JsonElement precipitation = parameters.GetProperty("PRECTOTCORR");

    double totalTemperature = 0;
    int validDays = 0;

    foreach (JsonProperty day in temperatures.EnumerateObject())
    {
        string date = day.Name;
        DateTime parsedDate = DateTime.ParseExact(date, "yyyyMMdd", CultureInfo.InvariantCulture);

        double temperature = day.Value.GetDouble();
        double precipitationValue = precipitation.GetProperty(date).GetDouble();

        if (temperature == -999 || precipitationValue == -999)
        {
            Console.WriteLine($"{parsedDate:yyyy-MM-dd}: Temperature/Precipitation data is missing.");
            continue;
        }

        totalTemperature += temperature;
        validDays++;

        Console.WriteLine($"{parsedDate:yyyy-MM-dd}: Temperature = {temperature} °C || Precipitation = {precipitationValue} mm");
    }

    if (validDays > 0)
    {
        double averageTemperature = totalTemperature / validDays;
        Console.WriteLine($"Average temperature for this period: {averageTemperature:F2} °C");
    }
}
catch (HttpRequestException ex)
{
    Console.WriteLine($"Request error: {ex.Message}");  
}
catch (JsonException ex)
{
    Console.WriteLine($"JSON parsing error: {ex.Message}");
}
catch (Exception ex)
{
    Console.WriteLine($"An error occurred: {ex.Message}");
}
