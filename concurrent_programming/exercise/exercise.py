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


# TODO: Implement the retrieve_data function
async def retrieve_data(urls: list[str]) -> list[str]:
    pass


async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    # TODO: Use the retrieve_data function to retrieve data from the provided URLs concurrently


if __name__ == "__main__":
    asyncio.run(main())
