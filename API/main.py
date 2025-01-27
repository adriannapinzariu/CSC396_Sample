from fastapi import FastAPI

app = FastAPI()

deliveries = []
next_id = 1

# Mock Data
deliveries = [
    {
        "id": next_id,
        "pickup_location": {"name": "Library", "latitude": 41.9249, "longitude": -87.6553},
        "dropoff_location": {"name": "Student Center", "latitude": 41.9228, "longitude": -87.6535},
        "status": "Completed",
        "distance": 0.30,
        "delivery_time": "2025-01-26T15:05:00"
    }
]

robots = [
    {
        "id": next_id,
        "current_location": {
            "latitude": 41.9249,
            "longitude": -87.6553
        },
        "status": "Available",
        "battery": 95.5,
        "max_load": 25.0
    },
    {
        "id": (next_id + 1),
        "current_location": {
            "latitude": 41.9228,
            "longitude": -87.6535
        },
        "status": "In Progress",
        "battery": 99.9,
        "max_load": 50.0
    }
]

# Get All Deliveries
@app.get("/deliveries")
async def get_all_deliveries():
    return deliveries

# Create a New Delivery
@app.post("/deliveries")
async def create_new_delivery():
    global next_id
    next_id += 1
    new_delivery = {
        "id" : next_id, #can you guys fix this in the documentation
        "pickup_location": {
            "name": "DePaul Art Museum",
            "latitude": 41.9252,
            "longitude": -87.6527
        },
        "dropoff_location": {
            "name": "Wish Field",
            "latitude": 41.9220,
            "longitude": -87.6565
        },
        "status": "Scheduled", #can you guys fix this in the documentation
        "distance": 0.25,
        "delivery_time": "2025-01-26T14:30:00" 
    }
    deliveries.append(new_delivery)
    return deliveries

# Get Delivery by ID
@app.get("/deliveries/{id}")
async def get_delivery_by_id(id: int):
    for delivery in deliveries:
        if delivery["id"] == id:
            return delivery

# Delete Delivery by ID
@app.delete("/deliveries/{id}")
async def delete_delivery_by_id(id: int):
    for delivery in deliveries:
        if delivery["id"] == id:
            deliveries.remove(delivery)
            return delivery 

# Someone help me with update please
'''
# Update a Delivery by ID
@app.patch("/deliveries/{id}")
async def update_delivery_by_id(id: int):
    # get deliveries list and id
    # go and check which one is different
    for delivery in deliveries:
        if delivery["id"] == id:
            updated_delivery = {
                "id": delivery["id"], # update this in documentation
                "pickup_location": {
                    "name": "Library",
                    "latitude": 41.9250,
                    "longitude": -87.6500
                },
                "dropoff_location": {
                    "name": "Student Center",
                    "latitude": 41.9200,
                    "longitude": -87.6600
                },
                "status": "Completed", # changed to completed
                "distance": 0.75,
                "delivery_time": "2025-01-26T15:05:00"
            }
        '''    

# Get All Robots
@app.get("/robots")
async def get_all_robots():
    return robots

# Create a New Robot
@app.post("/robots")
async def create_new_robot():
    new_robot = {
    	"id": 3, 
    	"current_location": { 
            "latitude": 41.4573, 
            "longitude": -87.0299, 
        },
    	"status": "Available", 
    	"battery": 100.0,
    	"max_load": 50.0 
    }
    robots.append(new_robot)
    return robots

# Get Robot by ID
@app.get("/robots/{id}")
async def get_robot_by_id(id: int):
    for robot in robots:
        if robot["id"] == id:
            return robot

# Delete Delivery by ID
@app.delete("/deliveries/{id}")
async def delete_delivery_by_id(id: int):
    for delivery in deliveries:
        if delivery["id"] == id:
            deliveries.remove(delivery)
            return delivery 

# Someone help me with update please


'''

static_string = "Initial test"

listUsers = { "Name": "Adrianna", "id" : 1 }, { "Name": "hehe", "id" : 2 }

@app.get("/user")
async def root():
    return listUsers

# use post to add data
@app.post("/user")
async def root(name: str = 0):
    listUsers.append({"name":name, "id": 3})
    return listUsers

@app.get("/")
async def hello(name: str):
    return {"Message": "Congrats! " + name + " This is your first API!"}

@app.get("/test")
async def read_root():
    return {"Message": "Congrats! This is your first API!"}

'''