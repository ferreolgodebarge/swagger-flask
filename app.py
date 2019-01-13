import sys
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version='1.0')

server = api.model(
    "server",
    {
        "uuid": fields.Integer(readOnly=True, description="Server id"),
        "server_details": fields.String(required=True, description="Server details")
    },
)

server_details = api.model(
        "server_details", 
        {
            "server_details": fields.String(required=True, description="Server details")
        },
)

class ServersDB(object):
    def __init__(self):
        self.counter = 0
        self.servers = []

    def get(self, uuid):
        for server in self.servers:
            if server["uuid"] == uuid:
                return server
        api.abort(404, "Server {} doesn't exist".format(uuid))

    def create(self, data):
        server = data
        server["uuid"] = self.counter + 1
        self.counter += 1
        self.servers.append(server)
        return server

    def update(self, uuid, data):
        server = self.get(uuid)
        server.update(data)
        return server

    def delete(self, uuid):
        server = self.get(uuid)
        self.servers.remove(server)

db = ServersDB()


@api.route("/servers")
class ServerList(Resource):
    @api.doc("list servers")
    @api.marshal_list_with(server)
    def get(self):
        return db.servers

    @api.doc("create server")
    @api.expect(server_details)
    @api.marshal_with(server, code=201)
    def post(self):
        return db.create(api.payload), 201


@api.route("/servers/<int:uuid>")
@api.response(404, "Server not Found")
@api.param("uuid", "Server unique identifier")
class Server(Resource):
    @api.doc("get server")
    @api.marshal_with(server)
    def get(self, uuid):
        return db.get(uuid)

    @api.doc("update server")
    @api.expect(server_details)
    @api.marshal_with(server)
    def put(self, uuid):
        return db.update(uuid, api.payload)

    @api.doc("delete server")
    @api.response(204, "Server Deleted")
    def delete(self, uuid):
        db.delete(uuid)
        return "", 204


if __name__ == "__main__":
    port = sys.argv[1]
    app.run(host="0.0.0.0", port=port, debug=True)
