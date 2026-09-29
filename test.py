from tools.tavily_tool import output_responce
from tools.flight_tool import search_flights
res=output_responce("Best Hotel in asia ")
ops=search_flights("Pakistan from china")
print(ops)
#print(res)