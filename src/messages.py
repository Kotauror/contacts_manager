from enum import Enum 

class Messages(Enum):
    ADD_SUCCESS = "Contact added successfully"
    ADD_ERROR = "Error: either name or telephone are already in the database"
    DELETE_SUCCESS = "Contact deleted successfully"
    DELETE_ERROR = "Error in deleting"
    EDIT_SUCCESS = "Contact edited successfully"
    EDIT_ERROR = "Error in editing"
