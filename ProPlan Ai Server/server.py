from fastapi import FastAPI
from Backend import backend as b 
from ai_response import ai_response as ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to ProPlan Ai Server"}


@app.get("/login")
def login(username: str, password: str):
    if not username:
        return {
            "status" : "error", 
            "message" : "Please enter Your Username."
        }
    if not password:
        return {
            "status": "error",
            "message" : "Please enter Your Password"
        }
    if len(username) < 6 or len(username) > 8:
        return {
            "status": "error",
            "message": "Please enter a valid username (6–8 characters)"
        }

    if len(password) < 6 or len(password) > 9:
        return {
            "status" : "error",
            "message" : "Please enter a valid Password (6-9 chracrers)"
        }
    data = b.login_account(username, password)

    return data

@app.get('/register')
def register(username:str, password:str, email:str):
    if not username:
        return {
            "status": "error",
            "message": "Please enter Your Username."
        }
    if not password:
        return {
            "status" : "error",
            "message" : "Please enter Your Password."
        }
    if not email:
        return {
            "status" : "error",
            "message" : "Please enter Your Email."
        }
    if b.check_email(email):
        data = b.register_account(username=username, password=password, email=email)

    return data

@app.get('/get_response')
def get_response(message:str):
    if not message:
        return{
            "status": "error",
            "message" : "Please enter Your Message."
        }
    
    try:
        data = ai.get_response(text=message)
        return data
    except Exception as e:
        return {
            'status' : 'error',
            'message' : e
        }
    
@app.get('/forget')
def forget(email:str):
    if not email:
        return {
            "status" : 'error',
            'message' : 'enter your email'
        }
    
    if b.check_email(email):
        pass
    return {
        "status" : "error",
        "message": "This not ablebloe now"
    }

@app.get('/get_plan')
def get_plan(projects_name:str, goals:str, category:str, selected_language:str):
    if not projects_name:
        projects_name = "You Create a name."
    if not goals:
        goals = "erarn many"
    if not category:
        category = "Ai/Ml"
    if not selected_language:
        selected_language = "Python"
    data = ai.get_plan(projects_name=projects_name, goals=goals, category=category, selected_language=selected_language)
    return data

4

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)