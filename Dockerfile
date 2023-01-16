#### docker image base환경 ex> python, nginx, ubuntu 등
# => 해당 docker build시 현재 image외 FROM에 적힌 base환경 image도 생긴다
FROM python:3.8
# python 기본 설정
ENV PYTHONUNBUFFERED 1

#### RUN: docker내부 환경설정 명령어들
RUN apt-get -y update
RUN apt-get -y install vim
# django app 폴더생성 - docker를 실행하면 /srv는 자동으로 생성되어있다 그 하위로 설정
RUN mkdir /srv/docker-server
# 파일복사- .(현재 Dockerfile이 있는 django프로젝트폴더)의 모든 내용을 => Docker의 /srv/docker-server폴더로 복사
ADD . /srv/docker-server

#### docker가 돌아가는 작업 디렉토리 - 만든 폴더로 경로이동(설정)
WORKDIR /srv/docker-server

#### 프로젝트폴더에 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#### django만 띄우는 경우를 위해 port를 EXPOSE로 설정 => 띄워지는거 확인되면 주석 처리 됨.
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



