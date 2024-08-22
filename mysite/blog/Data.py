import requests
import json


class Data:
    def getData(self):
        posts = [
            {
                "id": 1,
                "title": "House & Life Update…",
                "content": """Aliquam nec mi et nunc viverra dictum. Donec bendum tellus quis nisl efficiturut gravida mauris efficitur. Vestibulum alobortis nisi. \
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a sapien acbh sodales varius. Morbi endum libero. Nulla vestibulum, felis \
                            vitae aliquet dictum, nunc augue varius odio, imperdiet tincidunt neque metus ut lorem. Nunc non massa ornare, lobortis nunc vitae, \
                            hendrerit mauris. Vivamus nunc orci, vehicula sit amet tempus sit amet. Aliquam eleifend consequat est laoreet bibendum. Proin et nibh augue. \
                            Fusce condimentum vehicula condi entum. Nulla rutrum justo pellentesque nunc porta aliquam. Mauris sodales mauris sed mi elementum faucibus. \
                            Aliquam tinci dunt sem nec augue porta euismod. Nulla facilisi. Nulla ultricies ipsum massa, quis molestie magna acibus sed.Mauris sed risus \
                            facilisis, ullamcorper massa eu, elementum ligula. Vivamus sit amet risus i ornare finibus vitae ac nulla. Aenean eget ex ut libero congue \
                            rutrum a et diam. Mauris eu metus et nibh pulvinar tempus idefficitur dolor.""",
                "category": "Lifestyle",
                "postDate": "23/02/2020",
                "image_path": "images/blog/blog-md/blog/pic1.jpg",
            },
            {
                "id": 2,
                "title": "Crafts for Kids",
                "content": """Aliquam nec mi et nunc viverra dictum. Donec bendum tellus quis nisl efficiturut gravida mauris efficitur. Vestibulum alobortis nisi. \
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a sapien acbh sodales varius. Morbi endum libero. Nulla vestibulum, felis \
                            vitae aliquet dictum, nunc augue varius odio, imperdiet tincidunt neque metus ut lorem. Nunc non massa ornare, lobortis nunc vitae, \
                            hendrerit mauris. Vivamus nunc orci, vehicula sit amet tempus sit amet. Aliquam eleifend consequat est laoreet bibendum. Proin et nibh augue. \
                            Fusce condimentum vehicula condi entum. Nulla rutrum justo pellentesque nunc porta aliquam. Mauris sodales mauris sed mi elementum faucibus. \
                            Aliquam tinci dunt sem nec augue porta euismod. Nulla facilisi. Nulla ultricies ipsum massa, quis molestie magna acibus sed.Mauris sed risus \
                            facilisis, ullamcorper massa eu, elementum ligula. Vivamus sit amet risus i ornare finibus vitae ac nulla. Aenean eget ex ut libero congue \
                            rutrum a et diam. Mauris eu metus et nibh pulvinar tempus idefficitur dolor.""",
                "category": "Fashion",
                "postDate": "23/02/2020",
                "image_path": "images/blog/blog-md/blog/pic2.jpg",
            },
            {
                "id": 3,
                "title": "Packing to Orlando",
                "content": """Aliquam nec mi et nunc viverra dictum. Donec bendum tellus quis nisl efficiturut gravida mauris efficitur. Vestibulum alobortis nisi. \
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a sapien acbh sodales varius. Morbi endum libero. Nulla vestibulum, felis \
                            vitae aliquet dictum, nunc augue varius odio, imperdiet tincidunt neque metus ut lorem. Nunc non massa ornare, lobortis nunc vitae, \
                            hendrerit mauris. Vivamus nunc orci, vehicula sit amet tempus sit amet. Aliquam eleifend consequat est laoreet bibendum. Proin et nibh augue. \
                            Fusce condimentum vehicula condi entum. Nulla rutrum justo pellentesque nunc porta aliquam. Mauris sodales mauris sed mi elementum faucibus. \
                            Aliquam tinci dunt sem nec augue porta euismod. Nulla facilisi. Nulla ultricies ipsum massa, quis molestie magna acibus sed.Mauris sed risus \
                            facilisis, ullamcorper massa eu, elementum ligula. Vivamus sit amet risus i ornare finibus vitae ac nulla. Aenean eget ex ut libero congue \
                            rutrum a et diam. Mauris eu metus et nibh pulvinar tempus idefficitur dolor.""",
                "category": "travel",
                "postDate": "23/02/2020",
                "image_path": "images/blog/blog-md/blog/pic3.jpg",
            },
            {
                "id": 4,
                "title": "Love in Las Vegas",
                "content": """Aliquam nec mi et nunc viverra dictum. Donec bendum tellus quis nisl efficiturut gravida mauris efficitur. Vestibulum alobortis nisi. \
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a sapien acbh sodales varius. Morbi endum libero. Nulla vestibulum, felis \
                            vitae aliquet dictum, nunc augue varius odio, imperdiet tincidunt neque metus ut lorem. Nunc non massa ornare, lobortis nunc vitae, \
                            hendrerit mauris. Vivamus nunc orci, vehicula sit amet tempus sit amet. Aliquam eleifend consequat est laoreet bibendum. Proin et nibh augue. \
                            Fusce condimentum vehicula condi entum. Nulla rutrum justo pellentesque nunc porta aliquam. Mauris sodales mauris sed mi elementum faucibus. \
                            Aliquam tinci dunt sem nec augue porta euismod. Nulla facilisi. Nulla ultricies ipsum massa, quis molestie magna acibus sed.Mauris sed risus \
                            facilisis, ullamcorper massa eu, elementum ligula. Vivamus sit amet risus i ornare finibus vitae ac nulla. Aenean eget ex ut libero congue \
                            rutrum a et diam. Mauris eu metus et nibh pulvinar tempus idefficitur dolor.""",
                "category": "Beauty",
                "postDate": "23/02/2020",
                "image_path": "images/blog/blog-md/blog/pic4.jpg",
            },
            {
                "id": 5,
                "title": "Absolutely Romance",
                "content": """Aliquam nec mi et nunc viverra dictum. Donec bendum tellus quis nisl efficiturut gravida mauris efficitur. Vestibulum alobortis nisi. \
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a sapien acbh sodales varius. Morbi endum libero. Nulla vestibulum, felis \
                            vitae aliquet dictum, nunc augue varius odio, imperdiet tincidunt neque metus ut lorem. Nunc non massa ornare, lobortis nunc vitae, \
                            hendrerit mauris. Vivamus nunc orci, vehicula sit amet tempus sit amet. Aliquam eleifend consequat est laoreet bibendum. Proin et nibh augue. \
                            Fusce condimentum vehicula condi entum. Nulla rutrum justo pellentesque nunc porta aliquam. Mauris sodales mauris sed mi elementum faucibus. \
                            Aliquam tinci dunt sem nec augue porta euismod. Nulla facilisi. Nulla ultricies ipsum massa, quis molestie magna acibus sed.Mauris sed risus \
                            facilisis, ullamcorper massa eu, elementum ligula. Vivamus sit amet risus i ornare finibus vitae ac nulla. Aenean eget ex ut libero congue \
                            rutrum a et diam. Mauris eu metus et nibh pulvinar tempus idefficitur dolor.""",
                "category": "Beauty",
                "postDate": "23/02/2020",
                "image_path": "images/blog/blog-md/blog/pic5.jpg",
            },
        ]
        return posts

    def getPopularPosts(self):
        response = requests.get("http://127.0.0.1:8000/blog/popular")
        popular_json = response.json()
        data = json.loads(popular_json)
        return data
