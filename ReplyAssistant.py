# coding: utf-8

import praw

# Using a map instead an array in order to simplify things down the road...
# Should be pulled to an external file in the future...

# ReplyAssistantModule v1.0
# Last updated 2022-06-09

COMMON_REPLIES = {
    '[KEYWORD_1]': 'RESPONSE A', # YOU CAN USE MARKDOWN IN THE RESPONSE FIELDS
    '[KEYWORD_2]': 'RESPONSE B',
    '[KEYWORD_3]': 'RESPONSE C',
    '[KEYWORD_4]': 'RESPONSE D',
    '[KEYWORD_5]': 'RESPONSE E'
}

# As we are checking reddit post titles in lowercase, we need lowercase error codes to compare to...
COMMON_REPLIES = dict((k.lower(), v)
                            for k, v in COMMON_REPLIES.items())


def main():
    """
    Trampoline function for setup and new post event listener...
    :return: Nothing
    """
    # Ideally these keys should be pulled out to another file/put in an env variable and not committed to git...
    reddit = praw.Reddit(user_agent='Reply Assistant for Reddit Communities (by u/Falc0n2k)',
                         client_id='[YOUR_CLIENT_ID]', client_secret='[YOUR_CLIENT_SECRET]',
                         username='[ACCOUNT_YOU_WANT_TO_POST_BACK_AS]', password='[PASSWD_FOR_ACCT]')
    subreddit = reddit.subreddit('[SUBREDDIT]')

    print('Listening to posts...')
    print('')

    posts = 0
    for submission in subreddit.stream.submissions():
        print('Scanning post ' + submission.id + ' (' + str(posts) + ')...')
        posts += 1
        process_submission(submission)


def process_submission(submission):
    """
    Scans post title and checks for common error codes, replies if one is found...
    :param submission: The new reddit post
    :return: Nothing
    """
    # Force post title & body to lowercase...
    submission_title_and_body = submission.title.lower() + ' ' + \
        submission.selftext.lower()

    def get_common_error_code_mispellings(ec):
        """
        Small helper function to get common variations, such as in the case of error codes, taking into account spaces, hyphens, etc.
        :param ec: The code to make mispellings for...
        :return: Array with code and common mispellings...
        """
        return [ec, ' '.join(ec.split('-')), ''.join(ec.split('-')), ' - '.join(ec.split('-')),
                '- '.join(ec.split('-')), ' -'.join(ec.split('-'))]

    def get_formatted_reply(ec):
        """
        Small helper function to get formatted reply...
        Should be pulled to an external jinga template file in the future...
        :param ec: The code to make formatted reply for...
        :return: The formatted reply...
        """
        return '**[KEYWORD]**: `' + ec + '`\n\n**Description**: ' + COMMON_REPLIES[
            error_code] + '\n\n*^(I am a bot. I won’t respond to any replies to my comments.)*'

    # Go through each error code and see if it is in the post...
    for error_code in COMMON_REPLIES.keys():
        if any(ec in submission_title_and_body for ec in get_common_code_mispellings(error_code)):
            print('Found post (' + submission.id +
                  ') with error code ' + error_code)

            if any(top_level_comment.author == '[ACCT_YOU_WANT_TO_POST_BACK_AS]' and error_code.upper() in top_level_comment.body for
                   top_level_comment in submission.comments):
                print(
                    '  Already replied... Skipping.')
                print('')
                # Skip this error code, and continue to search for others in this post...
                continue

            print('  Replying to: ' + submission_title_and_body[:60] + '...')
            reply = get_formatted_reply(error_code.upper())
            print('  With reply : ' + reply[:27] + '...')
            print('')
            try:
                submission.reply(reply)
            except Exception as e:
                print(
                    '  Error replying. Attempting to continue...')
                print('  ' + str(e))
            print('')


if __name__ == '__main__':
    main()
