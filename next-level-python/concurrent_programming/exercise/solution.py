import asyncio


async def fetch(url: str) -> str:
    # Simulate network delay
    await asyncio.sleep(2)
    return f"Data from {url}"


async def retrieve_data(urls: list[str]) -> list[str]:
    tasks = [fetch(url) for url in urls]
    data = await asyncio.gather(*tasks)
    return data


async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    data = await retrieve_data(urls)
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
