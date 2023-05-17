#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from backend.app.api.v1.auth import router as auth_router
from backend.app.api.v1.user import router as user_router
from backend.app.api.v1.casbin import router as casbin_router
from backend.app.api.v1.dept import router as dept_router
from backend.app.api.v1.role import router as role_router
from backend.app.api.v1.menu import router as menu_router
from backend.app.api.v1.api import router as api_router
from backend.app.api.v1.task_demo import router as task_demo_router
from backend.app.api.v1.config import router as config_router

v1 = APIRouter(prefix='/v1')

v1.include_router(auth_router)
v1.include_router(user_router, prefix='/users', tags=['用户管理'])
v1.include_router(casbin_router, prefix='/casbin', tags=['权限管理'])
v1.include_router(dept_router, prefix='/depts', tags=['部门管理'])
v1.include_router(role_router, prefix='/roles', tags=['角色管理'])
v1.include_router(menu_router, prefix='/menus', tags=['菜单管理'])
v1.include_router(api_router, prefix='/apis', tags=['API管理'])
v1.include_router(config_router, prefix='/configs', tags=['系统配置'])
v1.include_router(task_demo_router, prefix='/tasks', tags=['任务管理'])
