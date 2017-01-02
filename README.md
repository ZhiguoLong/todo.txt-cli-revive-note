# Extension of revive and note add-ons for todo.txt
This is an extension of the add-ons [revive](https://github.com/duncanje/todo.txt-revive) and [note](https://github.com/mgarrido/todo.txt-cli/tree/note/todo.actions.d) for [todo.txt-cli](https://github.com/ginatrapani/todo.txt-cli). 

This extension allows one to easily re-add a completed task back to the todo.txt list, and it will restore the note (if any) associated to the task. **It will also remove the restored todo from the completed todos list.**

## Install
**Requires python.**

**Be aware that this add-on overrides the `archive`, `del` and `rm` commands.** If you already have overridden some of them, you'll need to do some tweaking to combine both versions.

Copy the `archive`, `del`, `rm`, `note`, `restorenote.py`, and `revive` files in this directory to your add-ons folder. The `revive` file provided here revises the original [revive](https://github.com/duncanje/todo.txt-revive). It adds the functionality of also restoring the note when restoring a todo. 

## Usage
List completed todos (from done.txt) available to revive:
```
todo.sh revive
```
Re-add a todo among the completed todos:
```
todo.sh revive ITEM#
```
For example:

```
$ todo.sh revive  
# shows a list of completed tasks
1 x 2017-01-01 A task with out note.  
2 x 2017-01-02 A task with a note. note:xyz.txt  
--  
DONE: 2 of 2 tasks shown  
$ todo.sh ls  
--  
TODO: 0 of 0 tasks shown 
$ todo.sh revive 2  
# restores completed task no. 2, where its note is automatically restored
2 add A task with a note. note:xyz.txt  
TODO: 2 added.  
TODO: 2 note restored. (xyz.txt)  
$ todo.sh revive  
# shows a list of completed tasks
1 x 2017-01-01 A task with out note.  
--  
DONE: 1 of 1 tasks shown  
$ todo.sh revive 1  
# restores completed task no. 1
1 A task with out note.  
TODO: 1 added.  
TODO: Task 1 has no note.  
```

The note file name will be automatically changed if there is already another note file with that name.

For more usage of the `note` add-on, see below or [the original project page](https://github.com/mgarrido/todo.txt-cli/tree/note/todo.actions.d).

>## Adding, viewing and editing notes
>
>* `note add|a ITEM#`. Adds a new note to task ITEM# and gives the chance to edit it.
>* `note edit|e ITEM#`. Opens the note related with task ITEM# in editor.
>* `note show|s ITEM#`. Shows the note related with task ITEM#.
>
>## The notes' archive
>
>When a done task is archived, the content of its note (if any) is appended to an archive file. This archive can be viewed or edited with the `show` and `edit` operations:
>
>* `note edit|e archive|a`. Opens in editor the notes' archive.
>* `note show|s archive|a`. Shows the notes' archive.
>
>The archive file is the only way to acces an archived task's note.
>
>## Deleted tasks
>
>When a task is deleted, its note (if any) is also also deleted.
>
>## Example of use
>```
>$ todo.sh ls
>1 Cook cake for birthday party
>2 Fix bicycle
>--
>TODO: 2 of 2 tasks shown
>```
>Say you're collecting recipes to prepare the cake from task 1 and want to write a note with the links to that recipes:
>```
>$ todo.sh note add 1
>1 Cook cake for birthday party note:cUn.txt
>TODO: Note added to task 1.
>Edit note?  (y/n)
>y
>```
>At this point, an editor is opened where you can enter any information related with task 1.
>
>Later on, you may want to see the content of the note of task 1:
>```
>$ todo.sh note show 1
># Cook cake for birthday party
>
>A couple of cakes thar look great:
>* http://www.terrificfantasticcakes.com/sacher
>* http://www.evenbettercakes.com/tartadesanmarcos
>```
>Perhaps you want to edit the note to add something else, then `todo.sh note edit 1` would open again the editor.
>
>## Configuration
>
>You can change the note file extension by adding an entry to your `todo.cfg` file:
>
>```
># Note file extension
>export TODO_NOTE_EXT=.md
>```

# License
MIT and GPL
