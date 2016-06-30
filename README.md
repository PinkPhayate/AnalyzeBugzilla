
#Bugzilla analyzer
---
You can extract bug status and comment from each report straged in Bugzilla.
URL: https://bugs.eclipse.org/bugs/show_bug.cgi?id=1789

## Environment
* OS X EI Capitan: v10.11.4
* Python: v2.7.11
* Anaconda: v2.5.0 (x86_64)


## HTML tag 
* 状態記述タグ
	```
	<span id="static_bug_status">	</span>
	```
* First of all, we extract elements from one of the table.
	```
	<td id="bz_show_bug_column_1" class="bz_show_bug_column">     
	```
* Next, we extract elements from another one.
	```
	<td id="bz_show_bug_column_2" class="bz_show_bug_column">
	```
* Extract ll comments
	```
	<pre class="bz_comment_text" >	</pre>
	```
    

