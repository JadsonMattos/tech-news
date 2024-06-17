NEWS = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
        "title": "noticia_0",
        "timestamp": "23/11/2020",
        "writer": "Escritor_0",
        "reading_time": 2,
        "summary": "Sumario da noticia_0",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "writer": "Eu",
        "summary": "Algo muito bacana aconteceu",
        "reading_time": 4,
        "timestamp": "04/04/2021",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia bacana 2",
        "writer": "Você",
        "summary": "Algo muito bacana aconteceu de novo",
        "reading_time": 1,
        "timestamp": "07/04/2022",
        "category": "Novidades",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_3.htm",
        "title": "noticia_3",
        "timestamp": "23/11/2020",
        "writer": "Escritor_3",
        "reading_time": 1,
        "summary": "Sumario da noticia_3",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_4.htm",
        "title": "noticia_4",
        "timestamp": "23/11/2020",
        "writer": "Escritor_4",
        "reading_time": 1,
        "summary": "Sumario da noticia_4",
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_5.htm",
        "title": "noticia_5",
        "timestamp": "23/11/2020",
        "writer": "Escritor_5",
        "reading_time": 1,
        "summary": "Sumario da noticia_5",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_6.htm",
        "title": "noticia_6",
        "timestamp": "23/11/2020",
        "writer": "Escritor_6",
        "reading_time": 1,
        "summary": "Sumario da noticia_6",
        "category": "Novidades",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_7.htm",
        "title": "noticia_7",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 7,
        "summary": "Sumario da noticia_1",
        "category": "Desenvolvimento web",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_8.htm",
        "title": "noticia_8",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 8,
        "summary": "Sumario da noticia_8",
        "category": "Desenvolvimento web",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 5,
        "summary": "Sumario da noticia_9",
        "category": "Linguagem de programação",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 5,
        "summary": "Sumario da noticia_9",
        "category": "Educação",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 5,
        "summary": "Sumario da noticia_9",
        "category": "Frameworks de programação",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "reading_time": 5,
        "summary": "Sumario da noticia_9",
        "category": "Educação",
    },
]

EXPECTED_NEWS = [(notice["title"], notice["url"]) for notice in NEWS]
