# MIT License
#
# Copyright (c) 2023 CyTheWorker
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from discord.app_commands import Group, command
# from discord.ext.commands import GroupCog

# # option 1 - this can be used inside a cog
# my_group = Group(name='group', description='description')
#
# @my_group.command()
# async def subcommand(interaction: Interaction):
#   ...
#
# subgroup = Group(parent=my_group, name='subgroup', description='description')
#
# @subgroup.command()
# async def subsubcommand(interaction: Interaction):
#   ...
#
# tree.add_command(my_group)
#
# # option 2 - this cannot be used inside a cog
# class MyGroup(Group, name='group', description='description'):
#   @command()
#   async def subcommand(self, interaction: Interaction):
#     ...
#
#   subgroup = Group(name='subgroup', description='description')
#
#   @subgroup.command()
#   async def subsubcommand(interaction: Interaction):
#     ...
#
# tree.add_command(MyGroup())
#
# # option 3 - this IS a cog
# class MyGroup(GroupCog, group_name='group', group_description='description'):
#   @command()
#   async def subcommand(self, interaction: Interaction):
#     ...
#
#   subgroup = Group(name='subgroup', description='description')
#
#   @subgroup.command()
#   async def subsubcommand(interaction: Interaction):
#     ...
#
# await bot.add_cog(MyGroup())  # this is the only time guild(s) kwarg is valid in add_cog