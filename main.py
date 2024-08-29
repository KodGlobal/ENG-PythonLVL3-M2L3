import discord
from discord.ext import commands
from logic import quiz_questions
# Task 7 - import the defaultdict command
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_responses = {}
# Task 8 - create thepoints dictionary to save user points


async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]
    buttons = question.gen_buttons()
    view = discord.ui.View()
    for button in buttons:
        view.add_item(button)

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')


@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        await interaction.response.send_message("Please start the quiz by typing the !start command")
        return

    custom_id = interaction.data["custom_id"]
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Correct answer!")
        # Task 9 - add points to user for correct answer
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Wrong answer!")

    # Task 5 - implement question counter
    # Task 6 - send user a message about the quiz result if they answered all questions. Otherwise, send the next question


@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id not in user_responses:
        user_responses[user_id] = 0
        await send_question(ctx, user_id)

bot.run(token)

