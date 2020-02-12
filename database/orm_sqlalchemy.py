#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean


engine = create_engine('mysql://root:lennon@localhost:3306/news?charset=utf-8')

base = declarative_base()

Session = sessionmaker(bind=engine)
