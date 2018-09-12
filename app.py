#-*- coding:utf-8 -*-
#!/usr/bin/env python

from apps import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
