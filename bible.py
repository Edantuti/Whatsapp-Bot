import requests
import os
from random import randint
apikey=os.environ.get('API')
class Bible:
  def verse_gen(self):
    book_id=['GEN', 'EXO', 'LEV', 'NUM', 'DEU', 'JOS', 'JDG', 'RUT', '1SA', '2SA', '1KI', '2KI', '1CH', '2CH', 'EZR', 'NEH', 'EST', 'JOB', 'PSA', 'PRO', 'ECC', 'SNG', 'ISA', 'JER', 'LAM', 'EZK', 'DAN', 'HOS', 'JOL', 'AMO', 'OBA', 'JON', 'MIC', 'NAM', 'HAB', 'ZEP', 'HAG', 'ZEC', 'MAL', 'MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM', '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH', '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE', '2PE', '1JN', '2JN', '3JN', 'JUD', 'REV']

    book_id_num = randint(0, len(book_id)-1)

    chapter_url = 'https://api.scripture.api.bible/v1/bibles/705aad6832c6e4d2-02/books/'+book_id[book_id_num]+'/chapters'

    chapter_data = requests.get(url=chapter_url, headers={
  'api-key':apikey
}).json()
    chapter_id = []
    for items in chapter_data['data']:
      chapter = items['id']
      if chapter[4:] != 'intro':
        chapter_id.append(chapter)

    chapter_id_num = randint(0, len(chapter_id)-1)

    passage_url = 'https://api.scripture.api.bible/v1/bibles/705aad6832c6e4d2-02/chapters/'+chapter_id[chapter_id_num]+'/verses'

    passage_data = requests.get(url=passage_url, headers={
  'api-key':apikey
}).json()

    passage_id = []

    for items in passage_data['data']:
      passage = items['id']
      passage_id.append(passage)

    verse_id_num = randint(0, len(passage_id)-1)

    verse_url ='https://api.scripture.api.bible/v1/bibles/705aad6832c6e4d2-02/verses/'+passage_id[verse_id_num]+'?content-type=json&include-notes=false&include-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include-verse-spans=false&use-org-id=false'

    verse_data = requests.get(url=verse_url, headers={
  'api-key':apikey
  }).json()
    verse_data_id=verse_data['data']['content']
    refer = verse_data['data']['reference']
    for items in verse_data_id:
      if len(items['items'])==2:
        verse = items['items'][1]
      else:
        verse = items['items'][0]
    
    return verse['text']+' '+refer


