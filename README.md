# Aya of the Day

Welcome to the `aya-of-day` project! This Python-based application tweets a random Aya (verse) from the Quran along with its translation daily. The project utilizes the Twitter API to post tweets and schedule daily updates.

## Features

- **Daily Tweets**: Automatically posts a random Aya from the Quran and its translation every day.
- **Threaded Tweets**: Handles long texts by splitting them into multiple tweets and linking them in a thread.
- **Customizable Scheduling**: Schedule the daily tweet at a specific time.

## Prerequisites

Before running the project, ensure you have the following:

- **Python 3.7+**
- **Twitter Developer Account**: Access to Twitter API keys.
- **Environment Variables**: Set up for Twitter API credentials.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zareshahi/aya-of-day.git
   cd aya-of-day
   ```

2. **Create a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root directory with the following content:

   ```env
   API_KEY=your_api_key
   API_SECRET_KEY=your_api_secret_key
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   BEARER_TOKEN=your_bearer_token
   ```

## Usage

1. **Running the Script**

   To test and send a tweet immediately, use:

   ```bash
   python main.py
   ```

   To schedule daily tweets, uncomment the `schedule_daily_tweet()` function call in the `main.py` file and run:

   ```bash
   python main.py
   ```

2. **Configuration**

   - **Daily Schedule**: The script is configured to send tweets daily at 20:00 Tehran time. Modify the schedule in the `schedule_daily_tweet` function if needed.

3. **Tweet Splitter**

   The `tweet_splitter` function from the `text_to_tweets` library ensures that long texts are split correctly to fit within Twitter’s character limits.

## File Structure

- **`main.py`**: The main script for sending tweets and scheduling.
- **`requirements.txt`**: List of Python dependencies.
- **`.env`**: Environment variables for Twitter API credentials.
- **`text_to_tweets.py`**: Contains the `tweet_splitter` function to handle text splitting.

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to:

- **Author**: [Your Name](https://github.com/zareshahi)

Thank you for checking out the `aya-of-day` project!
