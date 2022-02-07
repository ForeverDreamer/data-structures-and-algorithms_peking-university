"""
HJ19 简单错误记录

描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准

数据范围：错误记录数量满足  ，每条记录长度满足
输入描述：
每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述：
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入：
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
输出：
rzuwnjvnuz 633 1
atl 637 1
rwyfvzsopsuiqjnr 647 1
eez 648 1
fmwafhhgeyawnool 649 1
c 637 1
f 633 1
ywzqaop 631 2

说明：
由于D:\cfmwafhhgeyawnool 649的文件名长度超过了16个字符，达到了17，所以第一个字符'c'应该被忽略。
记录F:\fop\ywzqaop 631和F:\yay\jc\ywzqaop 631由于文件名和行号相同，因此被视为同一个错误记录，哪怕它们的路径是不同的。
由于循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准，所以D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645不会被记录。
"""

# input_seq = [
#     r'D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645',
#     r'E:\je\rzuwnjvnuz 633',
#     r'C:\km\tgjwpb\gy\atl 637',
#     r'F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647',
#     r'E:\ns\mfwj\wqkoki\eez 648',
#     r'D:\cfmwafhhgeyawnool 649',
#     r'E:\czt\opwip\osnll\c 637',
#     r'G:\nt\f 633',
#     r'F:\fop\ywzqaop 631',
#     r'F:\yay\jc\ywzqaop 631',
#     r'D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645',
# ]
input_seq = [
    r'D:\aibvjtrichmocux 629',
    r'E:\dwuz\cqvvntsgt 646',
    r'E:\klxxlxwcfkxfzoww 636',
    r'E:\gssfa\kx\eadgl 644',
    r'E:\eadgl 643',
    r'F:\sh\hv\bvqzgx 642',
    r'E:\ue\xhfx\fottgpgxuuzvya 629',
    r'G:\zg\ggm\ervybtevxbzg 639',
    r'E:\wirrmpbnbncyweutbj 648',
    r'G:\lo\uag\qdhlb\cqvvntsgt 649',
    r'E:\hvli\jynlilb 638',
    r'F:\ervybtevxbzg 646',
    r'C:\vzllig\rjhw\cqvvntsgt 629',
    r'E:\mj\imjtr\ervybtevxbzg 643',
    r'F:\ruyikv 633',
    r'G:\ifyuwf\erdvmu\mvymns 628',
    r'E:\lrlmx\ydh\jeckz\klxxlxwcfkxfzoww 633',
    r'E:\lzs\dlvd\lov\mvymns 639',
    r'G:\fr\khqb\ylq\ruyikv 640',
    r'C:\qcugk\yagcmu\zdqvru\xgsgwlkrp 633',
    r'G:\lcjpgv\cyylpn\sgvdd\jynlilb 638',
]


def error_record(seq):
    scanned_seq = []
    output_dict = {}
    idx = 0

    for s in seq:
        if s in scanned_seq:
            continue
        scanned_seq.append(s)
        path, line = s.split(' ')
        f_name = path.split('\\')[-1][:-17:-1][::-1]
        record = f_name + ' ' + line + ' 1'
        if record in output_dict:
            tmp_idx = output_dict[record]
            del output_dict[record]
            _, _, count = record.split(' ')
            record = f_name + ' ' + line + ' ' + str(int(count)+1)
            output_dict[record] = tmp_idx
        else:
            output_dict[record] = idx
            idx += 1

    output_seq = list(output_dict.items())
    output_seq.sort(key=lambda elem: elem[1])
    output_seq = [elem[0] for elem in output_seq]
    return output_seq[:-9:-1][::-1]


for item in error_record(input_seq):
    print(item)
