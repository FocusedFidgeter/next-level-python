# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Retrieve data from multiple URLs concurrently using asyncio
# Implement a function named retrieve_data to retrieve data from each of the provided URLs
# concurrently using asyncio and the fetch function.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import asyncio


async def fetch(url: str) -> str:
    # Simulate network delay
    await asyncio.sleep(2)
    return f"Data from {url}"


async def async_retrieve_data(urls: list[str]) -> list[str]:
    tasks = [
        fetch(url) for url in urls
    ]  # this is a list constructed from a for loop processing the `urls` list object.
    result = await asyncio.gather(*tasks)
    return result


async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    print(await async_retrieve_data(urls))


if __name__ == "__main__":
    asyncio.run(main())
