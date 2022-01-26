# 고양이 사진 검색 사이트 서버

## 환경
- python 3.9
- Django 3.2
- sqllite3

## 실행방법
```shell script
# 이미지 빌드, 컨테이너 생성 및 애플리케이션 시작 (데몬)
$ docker-compose up -d
```

## API
- 이미지 목록
```text
METHOD GET
URL    /api/animals/images
DATA
[
    {
        "id": int,
        "seq": int,
        "image": str,
        "created": datetime,
        "updated": datetime,
        "animal": int
    }
]
```

- 이미지 상세
```text
METHOD GET
URL    /api/animals/images/{ID}
DATA
{
    "id": int,
    "seq": int,
    "image": str,
    "created": datetime,
    "updated": datetime,
    "animal": int
}
```