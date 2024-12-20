from taskflowai import Agent
from src.agentic.utils.main_utils import LoadModel
from src.agentic.tools.serper_search import SerperSearch
from src.agentic.tools.wiki_search_articles import WikiArticles
from src.agentic.tools.wiki_search_images import WikiImages
from src.agentic.logger import logging
from src.agentic.exception import CustomException

class WebResearchAgent:
    @classmethod
    def initialize_web_research_agent(cls):
        """
        Initializes and returns the Web Research Agent.
        """
        try:
            logging.info("Initializing Web Research Agent.")
            web_research_agent = Agent(
                role="Web Research Agent",
                goal="Research destinations and find relevant images",
                attributes="diligent, thorough, comprehensive, visual-focused",
                llm=LoadModel.load_openai_model(),
                tools=[
                    SerperSearch.perform_search(),
                    WikiArticles.get_wiki_articles(),
                    WikiImages.get_wiki_images(),
                ],
            )
            logging.info("Web Research Agent initialized successfully.")
            return web_research_agent

        except Exception as e:
            logging.error("Error initializing Web Research Agent: %s", e)
            raise CustomException("Failed to initialize Web Research Agent.") from e
