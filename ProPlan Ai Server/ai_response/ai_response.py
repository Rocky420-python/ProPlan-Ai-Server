from openai import OpenAI


# project_name = self.project_name.get()
 #goals = self.goals.get()
 #category  = self.category.get()
 #selected_language = self.opt.get()

def get_response(text):
    api = "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"
    try:
        client = OpenAI(
        api_key=api,
        base_url="https://api.groq.com/openai/v1"
        )
        response = client.responses.create(
                    model="openai/gpt-oss-20b",
                    input=text
                )
        texts = response.output_text
        texts = texts.replace("ChatGPT", "ProPlanAI")
        texts = texts.replace("OpenAI", "RK AI")
        texts = texts.replace("ChatGPT", "ProPlan")
        return texts
    except Exception as e :
        return {
            "status" : 'error',
            "message" : e
        }
    
def get_plan(projects_name,goals,  category,selected_language ):
    api = "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"
    text = f"Hi Im a developer in {selected_language}, im just try to create new project, project name {projects_name}, my goals is {goals}, but i dont have a any plan you just create a plan my category {category}, you just create a plan not anything else."
    try:
        client = OpenAI(
            api_key=api,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=text
        )

        replay = response.output_text
        replay = replay.replace("ChatGpt", "ProPlan Ai ")
        text_response = replay
        return {
            "status" : "success",
            "message" : text_response
        }
    except Exception as e:
        return {
            "status": "error",
            "message" : e
        }