#coding: utf-8
''' mbinary
#######################################################################
# File : accountsMerge.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.xyz
# Github: https://github.com/mbinary
# Created Time: 2018-12-18  17:07
# Description: 
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该帐户的邮箱地址。

现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。

合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。

例子 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 "johnsmith@mail.com"。
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
#######################################################################
'''

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        mailDic = {}
        for ct,i in enumerate(accounts):
            for j in i[1:]:
                mailDic[j] = (ct,i[0])
        mails = {mail:idx  for idx,mail in enumerate(mailDic.keys())}
        mailNum = len(mails)
        self.findSet = [i for i in range(mailNum)]
        for li in accounts:
            n = len(li)
            for i in range(1,n-1):
                for j in range(i+1,n):
                    self.union(mails[li[i]],mails[li[j]])
        dic = {}
        mails = {j:i for i,j in mails.items()}
        for i in range(mailNum):
            mail = mails[i]
            n = mailDic[mails[self.find(i)]][0]
            if n in dic:
                dic[n].append(mail)
            else:
                dic[n] = [mail]
        nameId = {i[0]:i[1] for i in mailDic.values()}
        return [[nameId[i]]+sorted(mail) for i,mail in dic.items()]
    def find(self,i):
        if self.findSet[i]!=i:
            n = self.find(self.findSet[i])
            self.findSet[i] = n
        return self.findSet[i]
    def union(self,i,j):
        if i!=j:
            n = self.find(i)
            if n!=self.find(j):
                self.findSet[n] = self.findSet[j]

class Solution2:
    '''并查映射'''
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        mailDic = {j:ct for ct,i in enumerate(accounts) for j in i[1:]}
        self.findSet = {i:i for i in mailDic}
        for li in accounts:
            n = len(li)
            for i in range(1,n-1):
                for j in range(i+1,n):
                    self.union(li[i],li[j])
        dic = {}
        for mail in self.findSet:
            n = mailDic[self.find(mail)]
            if n in dic:
                dic[n].append(mail)
            else:
                dic[n] = [mail]
        return [[accounts[i][0]]+sorted(mail) for i,mail in dic.items()]
    def find(self,i):
        if self.findSet[i]!=i:
            n = self.find(self.findSet[i])
            self.findSet[i] = n
        return self.findSet[i]
    def union(self,i,j):
        if i!=j:
            n = self.find(i)
            if n!=self.find(j):
                self.findSet[n] = self.findSet[j]
