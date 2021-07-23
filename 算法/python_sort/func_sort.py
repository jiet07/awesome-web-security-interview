# -*- coding: UTF-8 -*-
#Space: https://github.com/Tri-x/exercise
#Space: https://space.bilibili.com/187492698
#Author: Trix
#Description: 十大经典排序算法

#Python的排序算法用的是Tim Sort 一种源自归并排序和插入排序的稳定高效的排序算法 也许以后会单独做一期视频来介绍该算法
#也许以后会做一期视频来介绍一些奇葩的排序算法 比如 睡眠排序、猴子排序、面条排序、珠排序

from random import randint#随机整数
from time import process_time#计时

nums_lists=[[]for n in range(4)]#随机创建四个无序数列 用来粗略地测试每种排序算法的用时
for n in range(500):#数列长度为500
	nums_lists[0].append(randint(-400,400))#随机范围(-400,400)
for n in range(1000):
	nums_lists[1].append(randint(-8000,8000))
for n in range(5001):
	nums_lists[2].append(randint(-2000,2000))
for n in range(10000):
	nums_lists[3].append(randint(-9000,9000))
#由于创建的随机数列太长,就不打印排序前和排序后的结果了


def bubble_sort(num_list):#冒泡排序 该算法名字的由来是因为越小的值会慢慢"浮"到数列的顶端
	#循环遍历数列,一次比较两个相邻的值,如果前者值大于后者值,就把他们的位置互相交换
	for n in range(len(num_list)-1):#因为最后一次已经顺序正确了所以循环次数-1
		for m in range(len(num_list)-1-n):
			#循环每结束一次 这一次循环中最大的值会移动到上一次循环中最大值的前一位 数列中后面的值已经有序 所以次数-n
			if num_list[m]>num_list[m+1]:#大小比较
				num_list[m+1],num_list[m]=num_list[m],num_list[m+1]#位置交换
	return num_list


def select_sort(num_list):#选择排序 选择最小值
	#每次循环在数列中找到最小值,放到上一次循环找到的最小值的后一位,第一次放在首位
	for n in range(len(num_list)-1):#因为最后一次已经顺序正确了所以循环次数-1
		min_index=n#设最小值为索引为n的值
		for m in range(n,len(num_list)):#n值前已完成排序
			if num_list[m]<num_list[min_index]:#最小值比较
				num_list[min_index],num_list[m]=num_list[m],num_list[min_index]#位置交换
	return num_list


def insert_sort(num_list):#插入排序 插入数值 此版本为插入排序最原始的版本
	#每次循环把索引为1的值到索引为第n次的值作为有序数列,把有序数列以外的每个值插入有序数列的正确位置
	for n in range(1,len(num_list)+1):#从第二个值开始
		for m in range(n):#每个值滚动的范围是其索引值
			if n<len(num_list):#防止n值超出数列长度
				if num_list[n]<=num_list[m]:#比较大小
					num_list[n],num_list[m]=num_list[m],num_list[n]#位置交换
	return num_list


def shell_sort(num_list):#希尔排序 插入排序的改进版 shell的音译
	#把整个无序数列按步长值分组,对每组数列分别进行插入排序,每次结束后减小步长,当步长值减小到1时对整个数列插入排序
	gap=len(num_list)//2#gap为步长值 //为除法向下取值
	while gap>=1:#控制步长范围
		#以下为插入排序的内容 并对插入排序进行了改进
		for n in range(gap,len(num_list)):
			while (n-gap)>=0:#控制比较范围
				if num_list[n]<num_list[n-gap]:#比较相邻两值大小
					num_list[n],num_list[n-gap]=num_list[n-gap],num_list[n]#位置交换
					n-=gap#把比较的两个值的索引向前移
				else:#超出索引范围后结束该循环
					break
		gap//=2#每次结束时减小步长值
	return num_list

def merge_sort(num_list):#归并排序 二分法 递归与合并
	#把无序数列递归地二分,直到只有两个或一个值为一组时,比较值的大小并排序,再返回这一组,
	#再递归地和其它组比较每个值的大小并排序,再返回排序的结果,再递归地返回成有序数列
	if len(num_list)<=1:#限制每组数列的最小长度
		return num_list
	middle=len(num_list)//2#二分值 //表示除法向下取整
	list_before=merge_sort(num_list[:middle])#数列前半部分为list_before 后半部分为list_after
	list_after=merge_sort(num_list[middle:])#这里最好自己举例一个有2或3个值的数列,初次遇见递归思想可能比较难理解
	'''
	比如运行merge_sort([3,2,1])
	[3,2,1]被分成了list_before=merge_sort([3])list_after=merge_sort([2,1])
		list_before=merge_sort([3]):merge_sort函数运行时,因为[3]长度等于1了 所以直接返回[3] 即list_before=[3]
		list_after=merge_sort([2,1]):merge_sort函数运行时,list_after=merge_sort
		在list_after该函数内部又二分成了list_before=merge_sort([2])list_after=merge_sort([1])
			与list_before=merge_sort([3])同理,在list_after该函数内部中,list_before=[2],list_after=[1]
			接着在list_after该函数内部中,执行return merge_compare(list_before,list_after)
			也就是比较[2]和[1]的大小后排序并返回 结果也就是list_after=[1,2]
		再执行return merge_compare(list_before,list_after)也就是比较[3]和[1,2]大小后排序并返回
		结果也就是return [1,2,3]
	最后返回总列表 其它数列以此类推
	'''
	return merge_compare(list_before,list_after)#返回list_before,list_after比较的结果

def merge_compare(list_before,list_after):#比较两个列表中的每个值
	result_list=[]#结果列表
	before_index=after_index=0#前列表和后列表数值的索引起始值
	while before_index<len(list_before) and after_index<len(list_after):#限制索引值
		if list_before[before_index]<list_after[after_index]:#如果前列表的值小于后列表的值
			result_list.append(list_before[before_index])#就把该值添加到结果列表
			before_index+=1#结束后索引值+1
		elif list_after[after_index]<=list_before[before_index]:#如果后列表的值小于等于前列表的值
			result_list.append(list_after[after_index])#同理
			after_index+=1
	if before_index==len(list_before):#如果前列表的索引值已经等于前列表长度了
		for n in list_after[after_index:]:#说明后列表的所有值大于前列表的最大值
			result_list.append(n)#因为后列表在递归中已经完成排序了 直接追加后列表
	elif after_index==len(list_after):#如果后列表的索引值已经等于后列表长度了
		for n in list_before[before_index:]:#同理
			result_list.append(n)
	return result_list#返回排序结果


def quick_sort(num_list):#调用快速排序的递归函数
	quick_recursion(num_list,0,len(num_list)-1)#传入数列,头索引值和尾索引值

def quick_recursion(num_list,head_index,tail_index):#快速排序 递归思想 建议和归并排序一样举例理解
	#从数列中任意挑选一个值(该值称为基准-Pivot),设置一个头索引值和尾索引值,用来限定扫描范围,头索引值向尾索引值移动
	#扫描每个值把所有小于基准值的数移到其前,所有大于基准的数移到其后(该步骤称为分区-Partition),再在每个分区里递归以上步骤
	if head_index<tail_index:#限制索引值
		pivot_index=quick_partition(num_list,head_index,tail_index)#获取基准所在索引值 这一步同时也完成了分区
		quick_recursion(num_list,head_index,pivot_index-1)#分别在前后分区范围内进行快速排序 因为基准值处于前分区结尾和后分区开头
		quick_recursion(num_list,pivot_index+1,tail_index)#所以对于前分区的尾索引值-1 对于后分区的头索引值+1
	return num_list

def quick_partition(num_list,head_index,tail_index):#比较大小并进行分区
	pivot=num_list[tail_index]#为了方便 选取该分区的结尾值作为基准-Pivot
	exchange_index=head_index-1#设置交换索引值 头索引值-1能把几种情况整合成一句代码
	for n in range(head_index,tail_index):#在两个索引值范围内 用基准值来区分每个值
		if num_list[n]<pivot:#如果扫描值小于基准值
			exchange_index+=1#控制交换索引值
			num_list[exchange_index],num_list[n]=num_list[n],num_list[exchange_index]#交换位置
	num_list[exchange_index+1],num_list[tail_index]=num_list[tail_index],num_list[exchange_index+1]#注意有个exchange_index+1
	'''
	比如quick_sort([1,4,5,6,3,4],0,5)
		在[1,4,5,6,3,4]中第一次分区时基准值=4,exchange_index=-1
			n=0时,扫描值1<基准值,exchange_index+1=0,再执行for循环时的下一行的交换位置的代码 等效于扫描值1的位置不变
			n=1时,扫描值4=基准值,exchange_index不变,exchange_index仍为0
			n=2时,扫描值5>基准值,exchange_index不变,exchange_index仍为0
			n=3时,扫描值6>基准值,exchange_index不变,exchange_index仍为0
			n=4时,扫描值3<基准值,exchange_index+1=1,再执行for循环时的下一行的交换位置的代码 等效于扫描值4和扫描值3交换位置
		此时for循环结束,执行for循环结束后的的下一行交换位置的代码 等效于扫描值5和基准值4交换位置
		第一次分区结束后我们得到了[1,3,4,6,4,5] partition函数返回了pivot_index=2
	接着在quick_sort函数内部继续运行quick_sort([1,3,4,6,4,5],0,2-1)和quick_sort([1,3,4,6,4,5],2+1,5)
	即对于[1,3]和[6,4,5]进行partition函数,同理 不赘述
	对于整个数列递归partition结束后 排序也就完成 其它数列以此类推
	'''
	return exchange_index+1#返回基准值所在的索引值


def heap_sort(num_list):#堆排序 完全二叉树 递归
	#递归地把数列形成每个父节点>每个左右子节点的完全二叉树
	#这样每次构建后索引[0]为最大值,在第n次结束,就把[0]和[-n]位置互换 在[0:-n-1]的范围内进行下次的完全二叉树构建
	list_len=len(num_list)#获取数列长度
	for n in range(list_len//2,-1,-1):
	#list_len//2为父节点索引的规律 //表示除法向下取整 n∈[list_len//2,-1),n∈Z range(start,stop,step) step为-1时为从后往前遍历
		heapify(num_list,list_len,n)#数列完全二叉树的初始化 构建每个父节点>每个左右子节点的完全二叉树
	for n in range(list_len-1,0,-1):#n∈[list_len-1,0),n∈Z
		num_list[0],num_list[n]=num_list[n],num_list[0]#对上一次构建完成的二叉树 首尾值互换
		list_len-=1#限定这一次构造完全二叉树的范围
		heapify(num_list,list_len,0)#由于已经初始化完成 可以直接从首项开始 在不包含上次最大值的范围内进行构造完全二叉树
	return num_list

def heapify(num_list,list_len,parent_index):#构建父节点>左右子节点的完全二叉树
	#第n排有n^(n-1),从左到右填充数值,可以得到父节点索引和左右子节点索引的规律
	left_index=2*parent_index+1#对于每个父节点索引 左节点索引的规律
	right_index=left_index+1#对于每个父节点索引 右节点索引的规律
	max_index=parent_index#假设父节点比左右子节点值都大 默认最大值的索引为父节点索引
	if left_index<list_len and num_list[left_index]>num_list[max_index]:#如果在列表范围内 左节点值>父节点值
		max_index=left_index#父节点和左节点的索引互换
	if right_index<list_len and num_list[right_index]>num_list[max_index]:#右节点同理
		max_index=right_index
	if max_index!=parent_index:#如果现在的父节点索引不等于一开始的假设的最大值的索引 说明父节点和它的某一节点需要互换索引值
		num_list[parent_index],num_list[max_index]=num_list[max_index],num_list[parent_index]
		heapify(num_list,list_len,max_index)#递归构建整个数列的完全二叉树


def count_sort(num_list):#计数排序 数数
	#找出数列中最大值和最小值 创建min~max这么多个0用来统计数列中每个值出现的次数,再从最小值依次排放到最大值
	max_num=max(num_list)#找到最大值
	min_num=min(num_list)#找到最小值
	neg_list=[]#负数数列
	pos_list=[]#非负数数列
	for num in num_list:#对负数和非负数分别处理
		if num<0:
			neg_list.append(num)#向负数数列添加负数
		if num>=0:
			pos_list.append(num)#向非负数数列添加非负数
	if len(neg_list)!=0:#如果有负数
		neg_counts_list=[0 for n in range(min_num,0)]#创建最小值这么多个0来累计每个负数出现的次数
		for n in range(len(neg_list)):#对于负数数列中的每个值
			neg_counts_list[neg_list[n]]+=1
		neg_index=0#初始排序索引为0
		for n in range(-len(neg_counts_list),0):#对于计数列表中的每一项
			while neg_counts_list[n]>0:#不为0就说明有计数 为0说明没有计数
				neg_list[neg_index]=n#依次排放数值
				neg_index+=1#每次排放后index+1
				neg_counts_list[n]-=1#每次排放后数值所对应的计数-1
	if len(pos_list)!=0:#如果有非负数
		pos_counts_list=[0 for n in range(max_num+1)]#创建max+1这么多个0来累计每个非负数出现的次数 因为是以每个值为索引 所以要max+1个0
		for n in range(len(pos_list)):#对于数列中的每个非负值
			pos_counts_list[pos_list[n]]+=1#计数列表索引和数列的值一一对应
		pos_index=0#初始排序索引为0
		for n in range(len(pos_counts_list)):#对于计数列表中的每一项
			while pos_counts_list[n]>0:#不为0就说明有计数 为0说明没有计数
				pos_list[pos_index]=n#依次排放数值
				pos_index+=1#每次排放后index+1
				pos_counts_list[n]-=1#每次排放后数值所对应的计数-1
	result_list=neg_list+pos_list#负数数列和非负数数列结合
	return result_list


def bucket_sort(num_list):#桶排序 计数排序的改进版
	#找出数列中最大值和最小值 创建min~max这么多个桶用来统计数列中每个值出现的次数,再从第一个桶倾倒到最后一个桶
	bucket_list=[0 for n in range(max(num_list)-min(num_list)+1)]#创建min~max这么多个桶
	for n in range(len(num_list)):#对于当前值
		bucket_list[num_list[n]-min(num_list)]+=1#添加到值对应的桶内 即对应桶计数+1
	result_list=[]#结果列表
	for n in range(len(bucket_list)):#对于每个桶
		if bucket_list[n]!=0:#如果桶内有数
			result_list+=[n+min(num_list)]*bucket_list[n]#直接把桶里的所有数倒出来
	return result_list


def radix_sort(num_list):#基数排序 比较位数上的值
	#比较每一位上的数字大小 当每一位比较完成排序也就完成
	pos_list=[]#负数数列
	neg_list=[]#非负数数列
	for num in num_list:#对负数和非负数分别处理
		if num<0:
			neg_list.append(num)
		if num>=0:
			pos_list.append(num)

	if len(neg_list)!=0:#如果有负数
		neg_num_digit=0#初始位数
		while neg_num_digit<len(str(min(neg_list))):#限制条件 当数的位数小于最小值位数时
			neg_values_lists=[[] for n in range(10)]#初始化数值列表 每位出现的值只可能是0~9 所以创建10个数值列表
			for neg_num in neg_list:#对于数列中的每个数
				neg_values_lists[int(neg_num/(10**neg_num_digit))%10].append(neg_num)
				#在第neg_num_digit+1次循环就比较该数的第n位上的数值 把该数添加到对应的数值列表 比如第一次循环就比较个位 第二次比较十位
			neg_list.clear()#清空原数列用来填充有序的数列
			for neg_value_list in neg_values_lists:#对于数值列表中的每个列表
				for neg_num in neg_value_list:#对于每个列表中的每个数
					neg_list.append(neg_num)
			neg_num_digit+=1#比较下一位

	if len(pos_list)!=0:#如果有非负数
		pos_num_digit=0#初始位数
		while pos_num_digit<len(str(max(pos_list))):#限制条件 当数的位数小于最大值位数时
			pos_values_lists=[[] for n in range(10)]#初始化数值列表 每位出现的值只可能是0~9 所以创建10个数值列表
			for pos_num in pos_list:#对于数列中的每个数
				pos_values_lists[int(pos_num/(10**pos_num_digit))%10].append(pos_num)
				#在第pos_num_digit+1次循环就比较该数的第n位上的数值 把该数添加到对应的数值列表比如第一次循环就比较个位 第二次比较十位
			pos_list.clear()#清空原数列用来填充有序的数列
			for pos_value_list in pos_values_lists:#对于数值列表中的每个列表
				for pos_num in pos_value_list:#对于每个列表中的每个数
					pos_list.append(pos_num)
			pos_num_digit+=1#比较下一位
	result_list=neg_list+pos_list#结果列表
	return result_list


#记录每一种排序算法对于不同长度无序数列的排序时间
sorts_time_dict={
			bubble_sort:['Bubble Sort'],#冒泡排序
			select_sort:['Select Sort'],#选择排序
			insert_sort:['Insert Sort'],#插入排序
			shell_sort:['Shell Sort'],#希尔排序
			merge_sort:['Merge Sort'],#归并排序
			quick_sort:['Quick Sort'],#快速排序
			heap_sort:['Heap Sort'],#堆排序
			count_sort:['Count Sort'],#计数排序
			bucket_sort:['Bucket Sort'],#桶排序
			radix_sort:['Radix Sort'],#基数排序
}


for num_list in nums_lists:#由于两层for循环会使对数列进行快速排序时的递归太深 会引起python崩溃 单独对每个数列进行快速排序
	print('正在对第'+str(nums_lists.index(num_list)+1)+'个'+'长为'+str(len(num_list))+'的随机数列执行Quick Sort算法')
	start_time=process_time()#开始计时 计时部分为排序算法
	quick_sort(num_list)
	end_time=process_time()#结束计时
	sorts_time_dict[quick_sort].append(end_time-start_time)#记录每种排序算法对不同长度数列的排序时间 单位为秒
for num_list in nums_lists:#对每个数列进行每一种排序算法
	for func_sort,time_list in sorts_time_dict.items():
		if func_sort!=quick_sort:
			print('正在对第'+str(nums_lists.index(num_list)+1)+'个'+'长为'+str(len(num_list))+'的随机数列执行'+time_list[0]+'算法')
			start_time=process_time()#开始计时 计时部分为排序算法
			func_sort(num_list.copy())#排序算法 .copy() 复制品 防止改变原数列
			end_time=process_time()#结束计时
			time_list.append(end_time-start_time)#记录每种排序算法对不同长度数列的排序时间 单位为秒
print()
print('十种排序算法对于不同长度的随机无序数列的排序时间结果如下:')
print('{:20s}{:<15d}{:<15d}{:<15d}{:<15d}'.format('Length of Series:',500,1000,5001,10000))#格式化输出
for time_list in sorts_time_dict.values():#每种算法
	for sort_time in time_list:#每种算法的名称和其处理每个数列的时间
		if not isinstance(sort_time,float):#如果use_time类型不为float 即为名称
			print('{:20s}'.format(sort_time+':'),end='')
		else:
			print('{:<15.4f}'.format(sort_time),end='')#左对齐 保留四位小数
	print()
print('单次随机数列排序时间结果不代表所有')
print()

count_sort_list=[]#因为计数排序太快了,单独创建一个长度为100000的数列来测试排序时间
for n in range(100000):
	count_sort_list.append(randint(-80000,100000))
start_time_count_sort=process_time()#开始计时 计时部分为排序算法
count_sort(count_sort_list.copy())
end_time_count_sort=process_time()#结束计时
print('计数排序一个长度为100000的随机数列所用时间为'+str(round(end_time_count_sort-start_time_count_sort,3))+'秒')
