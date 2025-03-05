from simple_blogger import CommonBlogger
from datetime import datetime

class Project(CommonBlogger):
    def _example_task_creator(self):
        return [
            {
                "group": "Group",
                "album": "Album",
                "song": "Spng",
            }
        ]

    def _get_category_folder(self, task):
        return f"{task['group']}"
                    
    def _get_topic_folder(self, task):
        return f"{task['song']}"

    def _system_prompt(self, task):
        return "Ты - блогер с 1000000 миллионном подписчиков"

    def _task_converter(self, idea):
        return { 
                    "song": idea['song'],
                    "album": idea['album'],
                    "group": idea['group'],
                    "topic_prompt": f"Расскажи про песню '{idea['song']}' c альбома '{idea['album']}' группы '{idea['group']}', используй не более {self.topic_word_limit} слов, используй смайлики",
                    "topic_image": f"Нарисуй рисунок, вдохновлённый песней '{idea['song']}' c альбома '{idea['album']}' группы '{idea['group']}'",
                }

    def __init__(self, **kwargs):
        super().__init__(
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 3, 7),
            text_ai_token_name='OPENAI_API_KEY',
            ai_text_model='chatgpt-4o-latest',
            text_base_url='https://api.openai.com/v1',
            topic_word_limit=100,
            **kwargs
        )