from simple_blogger import CommonBlogger
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import datetime
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.InstagramSender import InstagramSender
from simple_blogger.senders.VkSender import VkSender


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
            first_post_date=datetime(2025, 2, 22),
            text_generator=OpenAITextGenerator(),
            topic_word_limit=100,
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id=f"@meloman_the"), 
                     InstagramSender(channel_token_name='MELOMAN_THE_TOKEN'),
                     VkSender(group_id="229821806")
                     ],
            **kwargs
        )   
   