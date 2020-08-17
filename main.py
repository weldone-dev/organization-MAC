import requests 
import csv
def main(start = 0, size = 50, total=None):
    url = "https://services13.ieee.org/RST/standards-ra-web/rest/assignments/"
    r = requests.get(f"{url}?registry=MAC&text=&sortby=organization&sortorder=asc&size=1&from=1)").json()  
    if not(total):
        total = r["data"]["totalHits"]
    all_info = []
    print(f"Total {total}")
    for _ in range(int(total/size)):
        print(f"\rfrom {start}", end="")
        r = requests.get(f"{url}?registry=MAC&text=&sortby=organization&sortorder=asc&size={size}&from={start}").json()
        mac_organization = {}
        rp = r["data"]["hits"]
        for p in rp:
            all_info.append(p)
        start += size
    return all_info
def to_in_csv(all_info):
    with open("MAC.csv", mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
       
        print("start")
        for e in all_info:
            writer.writerow([str(e["assignmentNumberHex"]),
                e["organizationName"].strip(), 
                e["requestType"].strip(), 
            ])
        print("done")

if __name__ == "__main__":
    to_in_csv(main(size=int(39736/60)))

    




