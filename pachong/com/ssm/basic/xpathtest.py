from lxml import etree

if __name__ == '__main__':
    tree = etree.parse('1.html')
    #  r = tree.xpath('/html/body/h1')
    # r = tree.xpath('//h1')
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="song"]//li[5]/a/text()')[0]
    # r = tree.xpath('//li[7]//text()')
    # r = tree.xpath('//div[@class="song"]//text()')
    r = tree.xpath('//div[@class="song"]/img/@src')
    print(r)
