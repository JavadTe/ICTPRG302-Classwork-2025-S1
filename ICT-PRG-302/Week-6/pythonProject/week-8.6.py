week_rainfall = {
  "Mon":0,
  "Tue":3,
  "Wed":7,
  "Thu":1,
  "Fri":2,
  "Sat":6,
  "Sun":23
}
total_rain = 0
for day, rainfall in week_rainfall.items():
    total_rain = rainfall + total_rain
print(total_rain, "mm")

