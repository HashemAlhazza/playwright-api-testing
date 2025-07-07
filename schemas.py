LIST_USERS_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string", "format": "uri"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string", "format": "uri"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        }
    },
    "required": ["data"]
}

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

UPDATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["name", "job", "updatedAt"]
}

RESOURCE_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "year": {"type": "integer"},
                    "color": {"type": "string"},
                    "pantone_value": {"type": "string"}
                },
                "required": ["id", "name", "year", "color", "pantone_value"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

SINGLE_RESOURCE_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "color": {"type": "string"},
                "pantone_value": {"type": "string"}
            },
            "required": ["id", "name", "year", "color", "pantone_value"]
        }
    },
    "required": ["data"]
}

SUCCESSFUL_REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

UNSUCCESSFUL_REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

SUCCESSFUL_LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

UNSUCCESSFUL_LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

DELAYED_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string", "format": "uri"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string", "format": "uri"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        }
    },
    "required": ["data"]
}

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

UPDATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string", "format": "date-time"}
    },
    "required": ["name", "job", "updatedAt"]
}

RESOURCE_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "year": {"type": "integer"},
                    "color": {"type": "string"},
                    "pantone_value": {"type": "string"}
                },
                "required": ["id", "name", "year", "color", "pantone_value"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

SINGLE_RESOURCE_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "color": {"type": "string"},
                "pantone_value": {"type": "string"}
            },
            "required": ["id", "name", "year", "color", "pantone_value"]
        }
    },
    "required": ["data"]
}

SUCCESSFUL_REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

UNSUCCESSFUL_REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

SUCCESSFUL_LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

UNSUCCESSFUL_LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

DELAYED_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string", "format": "uri"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}