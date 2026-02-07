# API Fetcher Tool

A modular and extensible command-line tool for fetching data from public APIs, validating responses, and generating clean output reports.

## Features

- Fetch data from predefined API endpoints
- Support for query parameters (`--params key=value`)
- Automatic JSON validation
- Error handling for:
  - Timeout
  - HTTP errors
  - Invalid responses
- Save full API response to `output/response.json`
- Generate summary report in `output/summary.txt`
- Modular architecture (fetcher, validator, reporter, CLI)

## Project Structure

