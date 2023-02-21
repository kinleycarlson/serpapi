import json
import csv

###dumping to csv file:
infile = open("serp_results.json", "r")
results_data = json.load(infile)
results_list = results_data["local_results"]
print(results_list[0])
outfile = open("serp_results.csv", "w")

outfile.write(
    f"Position, Title, Place ID, Place ID Search, lsig, Rating, Original Reviews, Reviews, Type, Years in Business, Address, Phone, Hours, Latitude, Longitude, Website, Directions \n"
)

for result in results_list:
    position = result["position"]
    title = result["title"]
    place_id = result["place_id"]
    place_id_search = result["place_id_search"]
    lsig = result["lsig"]
    rating = result["rating"]
    reviews_original = result["reviews_original"]
    reviews = result["reviews"]
    type = result["type"]
    phone = result["phone"]
    latitude = result["gps_coordinates"]["latitude"]
    longitude = result["gps_coordinates"]["longitude"]

    if "years_in_business" in result.keys():
        years_in_business = result["years_in_business"]
    else:
        years_in_business = "years in business not found"

    if "address" in result.keys():
        address = result["address"]
    else:
        address = "address not found"

    if "hours" in result.keys():
        hours = result["hours"]
    else:
        hours = "hours not found"

    # if "online_estimates" in result.keys():
    #  online_estimates = result["service_options"]["online_estimates"]
    links_data = result["links"]
    if "website" in links_data.keys():
        website = links_data["website"]
    else:
        website = "no website link found"
    if "directions" in links_data.keys():
        directions = links_data["directions"]
    else:
        directions = "no directions link found"

    outfile.write(
        f"{position}, {title}, {place_id}, {place_id_search}, {lsig}, {rating}, {reviews_original}, {reviews}, {type}, {years_in_business}, {address}, {phone}, {hours}, {latitude}, {longitude}, {website},{directions} \n"
    )
