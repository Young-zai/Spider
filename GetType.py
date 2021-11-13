#获取电影类型
import requests
class Type(object):

    def __init__(self) -> None:
        super().__init__()

    
    def Getting_movietype(self):
        url = 'https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Referer': 'https://ys.endata.cn/BoxOffice/Ranking'
        }
        data = {
            'r': '0.4237929329022021',
            'top': '50',
            'type': '0'
        }
        response = requests.post(url=url,headers=headers,data=data)
        detail_data = response.json()
        movie_ID = []
        movie_type = []
        for dic in detail_data['data']['table0']:
            movie_ID.append(dic['EnMovieID'])
        
        for id in movie_ID:
            type_url = 'https://ys.endata.cn/enlib-api/api/movie/getMovie_HeadDetailByMovieID.do'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                'Referer': 'https://ys.endata.cn/Details/Movie?entId=id'
            }
            data = {
                'r': '0.7980670325061587',
                'entmovieid': id
            }
            response =  requests.post(url=type_url,headers=headers,data=data)
            type_data = response.json()
            type_data = type_data['data']['table0']
            
            for i in type_data:
                movie_type.append(i['Genre'])
        return movie_type
        


