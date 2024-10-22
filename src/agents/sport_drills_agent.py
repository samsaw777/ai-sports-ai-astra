from langchain_openai import ChatOpenAI
from src.config.settings import Settings
from langchain_core.prompts import PromptTemplate

settings = Settings()

class SportAgent:
    @staticmethod
    async def generate_sports_drills(sport_name: str, skill_level: str):
        """Agent to create sports drills"""
        try:
            model = ChatOpenAI(api_key=settings.OPENAI_API_KEY, model=settings.MODEL_NAME)

            prompt_template = PromptTemplate(
                input_variables=["sportName", "sportSkillLevel"],
                template="""
                You are an expert in coaching {sportName}. 
                Your task is to create a set of drills for the user.
                The user is a {sportSkillLevel} player.
                Generate a set of drills that include:
                - Warm-up drills
                - Skill drills
                - Conditioning drills
                - Cool-down drills 

                Drils should all be in list format.
                """
            )

            prompt = prompt_template.format(sportName=sport_name, sportSkillLevel=skill_level)
            response = model.invoke([{"role": "user", "content": prompt}])
            
            return {"drills": response.content}  # Properly format the response
            
        except Exception as e:
            return {"error": str(e)}