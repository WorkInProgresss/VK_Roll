from googleapiclient.discovery import build


def d_quer(query):

    d_se = '014347923427048117103:dy1-8_r54qw'
    m_se = '014347923427048117103:c_uvq12pwc8'

    res = search(query,m_se)
    n_res = int(res['searchInformation']['totalResults'])

    if n_res == 0:
        res = search(query,d_se)
        n_res = int(res['searchInformation']['totalResults'])

        if n_res == 0:
            return 'Никаких тебе ссылок. Нет ничего.'

        else:
            link = res['items'][0]['link']
            return link

    else:
        link = res['items'][0]['link']
        return link


def search(query,se):

    service = build('customsearch', 'v1',
                    developerKey='AIzaSyC6RdXDP8-63gLyJPR1nWqNzglFIoWzVLo')
    res = service.cse().list(
        q=query,
        cx=se,
    ).execute()

    return res

