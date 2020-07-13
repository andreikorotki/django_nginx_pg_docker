from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from web.models import Publication

publications_data = [
    {
        'id': 0,
        'title': 'Название',
        'date': datetime.now(),
        'text': '<b>Lorem Ipsum</b> - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" <br>для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.',
        'comments': [{'id': 0,
                      'nickname': 'Andy',
                      'comment_date': datetime.now(),
                      'comment_text': 'asd',
                      },
                     {'id': 1,
                      'nickname': 'Andy3',
                      'comment_date': datetime.now(),
                      'comment_text': 'asdwww',
                      }]
    },
    {
        'id': 1,
        'title': 'Название 2',
        'date': datetime.now(),
        'text': 'Text 2 Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" <br>для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'
    },
]

feedbacks = [
    {
        'id': 0,
        'contact_email': 'Название',
        'date': datetime.now(),
        'text': '<b>Lorem Ipsum</b> - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" <br>для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'
    },
    {
        'id': 1,
        'contact_email': 'Название 2',
        'date': datetime.now(),
        'text': 'Text 2 Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" <br>для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'
    },
]


def index(request):
    return render(request, 'main.html')


def contacts(request):
    if request.method == 'POST':
        contact_email = request.POST.get('contact_email')
        text = request.POST.get('text')
        if contact_email and text:
            feedbacks.append({
                'id': len(feedbacks),
                'contact_email': contact_email,
                'date': datetime.now(),
                'text': text
            })
            return redirect('/sendfeedback')
        else:
            return render(request, 'contacts.html', {
                'error': 'contact_email и text должны быть не пустыми'
            })
    else:
        return render(request, 'contacts.html')


def sendfeedback(request):
    return render(request, 'sendfeedback.html')


def post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            p = Publication.objects.create(title=title, text=text)
            p.save()
            return redirect('/publications')
        else:
            return render(request, 'post.html', {
                'error': 'title и text должны быть не пустыми'
            })
    return render(request, 'post.html')


def publications(request):
    publications_sorted = Publication.objects.all().order_by('-date')
    return render(request, 'publications.html', {
        'publications': publications_sorted
    })


def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/')
    return render(request, 'publication.html', {
        'publication': publication
    })


def status(request):
    return HttpResponse("Status OK")
