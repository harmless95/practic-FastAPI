import asyncio

from celery.bin.result import result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from sqlalchemy.orm import selectinload, joinedload

from library_project.core_app.models import db_helper, User, Profile, Post


async def create_user(session: AsyncSession, user_name: str, user_surname: str) -> User:
    user = User(user_name=user_name, user_surname=user_surname)
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def get_user_by_username(
    session: AsyncSession, user_name: str, user_surname: str = None
) -> User | None:
    condition = [User.user_name == user_name]
    if user_surname is not None:
        condition.append(User.user_surname == user_surname)
    stmt = select(User).where(*condition)
    result: Result = await session.execute(stmt)
    user: User | None = result.scalar_one_or_none()
    print("found user", user_name, user)
    return user


async def create_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession) -> list[User]:
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    # user = result.scalars().first()
    users = await session.scalars(stmt)
    for user in users:
        print(user)
        print(user.profile.first_name)


async def create_post(
    session: AsyncSession,
    user_id: int,
    *posts_titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in posts_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_posts(
    session: AsyncSession,
):
    # stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    stmt = select(User).options(selectinload(User.posts)).order_by(User.id)
    # users = await session.scalars(stmt)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    for user in users:
        print("**" * 10)
        print(user)
        for post in user.posts:
            print("-", post)


async def get_post_with_author(session: AsyncSession):
    stmt = select(Post).options(joinedload(Post.user)).order_by(Post.id)
    posts = await session.scalars(stmt)
    for post in posts:
        print("post", post)
        print("author", post.user)


async def get_users_posts_and_profile(session: AsyncSession):
    stmt = (
        select(User)
        .options(
            joinedload(User.profile),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = await session.scalars(stmt)
    for user in users:
        print("**" * 10)
        print(user, user.profile and user.profile.first_name)
        for post in user.posts:
            print("-", post)


async def get_profiles_with_users_and_users_with_posts(session: AsyncSession):
    stmt = (
        select(Profile)
        .join(User)
        .options(joinedload(Profile.user).selectinload(User.posts))
        .where(User.user_name == "vit")
        .order_by(Profile.id)
    )
    profiles = await session.scalars(stmt)
    for profile in profiles:
        print(
            profile.first_name,
            profile.user,
        )
        print(profile.user.posts)


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, user_name="vit", user_surname="zah")
        # await create_user(session=session, user_name="alice", user_surname="Smith")
        # user_vit = await get_user_by_username(session=session, user_name="vit")
        # # # await get_user_by_username(session=session, user_name="tt")
        # user_john = await get_user_by_username(
        #     session=session, user_name="john", user_surname="Smith"
        # )
        # await create_profile(
        #     session=session,
        #     user_id=user_vit.id,
        #     first_name=user_vit.user_name,
        # )
        #
        # await create_profile(
        #     session=session,
        #     user_id=user_john.id,
        #     first_name=user_john.user_name,
        #     last_name=user_john.user_surname,
        # )
        # await show_users_with_profiles(session=session)
        # await create_post(
        #     session,
        #     user_vit.id,
        #     "SQL 2.0",
        #     "SQL VIT",
        # )
        # await create_post(
        #     session,
        #     user_john.id,
        #     "FASTAPI intro",
        #     "FASTAPI advanced",
        #     "FastAPI more",
        # )
        # await get_posts(session=session)
        # await get_post_with_author(session=session)
        # await get_users_posts_and_profile(session=session)
        await get_profiles_with_users_and_users_with_posts(session=session)


if __name__ == "__main__":
    asyncio.run(main())
