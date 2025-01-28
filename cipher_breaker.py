def evk(a,b): #расширенный алгоритм евклида
    if b>a:
        a,b=b,a
    x2=1
    x1=0
    y2=0
    y1=1
    while b!=0:
        q=a//b
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1

        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    return (a,x2,y2) #НОД,х,у из ax+by=НОД

def a_1(a,m): #нахождение обратного элемента a по mod m
    d,x,y=evk(m,a)
    if d>1:
        return 0
    elif d==1:
        return y%m
    
def r(s,k1,k2): # функция для расшифрования
    y1 = [a.index(i) for i in s] #преобразуем буквенную строчку в числовую
    x1=[]
    for i in y1:
        k1[0]=a_1(k1[0],len(a)) #найдем обратный элемент а
        if not k1[0]:
            return 0
        x1.append((i-k1[1])*k1[0]%len(a)) #расшифруем и добавим в ответ символ
        k=[k1[0]*k2[0],k1[1]+k2[1]] # формируем новый ключ
        k1=k2
        k2=k
    x2 = [a[i] for i in x1] #преобразуем числовую строчку в буквенную
    x3=''
    for i in x2:
        x3+=i
    return x3


#Создаем массив самых популярных английских слов
m=['absolute', 'accept', 'account', 'accountant', 'achieve', 'acquire', 'act', 'action', 'activity', 'actor', 'actress', 'acute', 'add', 'address', 'admit', 'adopt', 'adult', 'affect', 'age', 'aged', 'agree', 'aim', 'air', 'allow', 'alone', 'alphabet', 'amount', 'ample', 'analysis', 'ancient', 'angry', 'animal', 'announce', 'answer', 'appear', 'application', 'apply', 'appoint', 'approach', 'apt', 'area', 'argue', 'arise', 'arm', 'army', 'arrange', 'arrive', 'art', 'ask', 'aspect', 'assess', 'associate', 'association', 'assume', 'attempt', 'attend', 'attract', 'authority', 'autumn', 'average', 'avoid', 'award', 'baby', 'back', 'bad', 'bald', 'bank', 'bare', 'base', 'be', 'bear', 'beat', 'become', 'bed', 'begin', 'believe', 'belong', 'benefit', 'big', 'black', 'bland', 'blank', 'bleak', 'blind', 'blond', 'bloody', 'blue', 'blunt', 'board', 'body', 'bold', 'book', 'boring', 'born', 'boy', 'brave', 'break', 'brief', 'bright', 'bring', 'brisk', 'broad', 'brother', 'brown', 'build', 'builder', 'building', 'bulky', 'business', 'busy', 'buy', 'call', 'calm', 'capital', 'car', 'care', 'carry', 'casual', 'cat', 'catch', 'cause', 'cd player', 'ceiling', 'central', 'century', 'chair', 'chairman', 'change', 'chapter', 'charge', 'cheap', 'check', 'cheeky', 'chief', 'child', 'childish', 'chilly', 'choose', 'church', 'circumstance', 'city', 'claim', 'class', 'classroom', 'clean', 'cleaner', 'clear', 'clever', 'client', 'close', 'club', 'clumsy', 'coarse', 'cold', 'collect', 'college', 'come', 'commission', 'commit', 'committee', 'community', 'compact', 'company', 'compare', 'complete', 'computer', 'concentrate', 'condition', 'conference', 'confirm', 'consider', 'consist', 'contain', 'continue', 'contract', 'contribute', 'control', 'cool', 'corrupt', 'cost', 'costly', 'cosy', 'cough', 'council', 'country', 'couple', 'course', 'court', 'cover', 'crazy', 'create', 'crisp', 'cross', 'crude', 'cruel', 'cry', 'cunning', 'cupboard', 'curious', 'curved', 'customer', 'cut', 'daft', 'damp', 'data', 'date', 'daughter', 'day', 'dead', 'deadly', 'deaf', 'deal', 'dear', 'death', 'decide', 'decision', 'deep', 'define', 'deliver', 'demand', 'demonstrate', 'deny', 'department', 'depend', 'describe', 'design', 'detail', 'determine', 'develop', 'development', 'dictionary', 'die', 'dim', 'dire', 'direction', 'director', 'dirty', 'discover', 'discreet', 'discuss', 'discussion', 'disease', 'divine', 'division', 'dizzy', 'do', 'doctor', 'dog', 'dollar', 'door', 'draw', 'dress', 'drink', 'drive', 'drop', 'drug', 'drunk', 'dry', 'dull', 'dumb', 'dusty', 'duty', 'dvd player', 'early', 'easy', 'eat', 'economy', 'education', 'effect', 'effort', 'eight', 'eighteen', 'election', 'eleven', 'emerge', 'employ', 'empty', 'enable', 'encourage', 'end', 'engineer', 'enjoy', 'ensure', 'enter', 'environment', 'establish', 'evening', 'event', 'evidence', 'examine', 'example', 'exist', 'expect', 'experience', 'explain', 'express', 'extend', 'extreme', 'eye', 'face', 'factor', 'fail', 'faint', 'fair', 'fall', 'family', 'fancy', 'far', 'fast', 'fat', 'father', 'fatty', 'feed', 'feel', 'field', 'fierce', 'fiery', 'fifteen', 'fight', 'figure', 'fill', 'film', 'filthy', 'find', 'fine', 'finish', 'fire', 'firm', 'fit', 'five', 'flat', 'floor', 'floppy', 'flu', 'fly', 'follow', 'fond', 'foot', 'force', 'forget', 'form', 'foul', 'four', 'fourteen', 'frail', 'frank', 'free', 'fresh', 'friday', 'friend', 'friendly', 'full', 'fund', 'funny', 'furniture', 'future', 'gain', 'game', 'garden', 'gay', 'get', 'ghastly', 'girl', 'give', 'glad', 'gloomy', 'glossy', 'go', 'going', 'gold', 'good', 'government', 'grand', 'grant', 'grave', 'greasy', 'great', 'greedy', 'green', 'grey', 'grim', 'gross', 'ground', 'grow', 'guilty', 'hair', 'hairy', 'hall', 'hand', 'handsome', 'handy', 'hang', 'happen', 'happy', 'hard', 'hardy', 'harsh', 'hate', 'have', 'head', 'headache', 'health', 'healthy', 'hear', 'heart', 'heavy', 'help', 'hide', 'high', 'history', 'hit', 'hold', 'hollow', 'holy', 'home', 'honest', 'hope', 'horse', 'hospital', 'hot', 'hotel', 'hour', 'house', 'housewife', 'huge', 'hundred', 'hungry', 'husband', 'idea', 'identify', 'ignore', 'ill', 'imagine', 'impose', 'improve', 'include', 'income', 'increase', 'indicate', 'industry', 'infection', 'information', 'insist', 'institution', 'intend', 'interest', 'introduce', 'investment', 'invite', 'involve', 'issue', 'job', 'join', 'joint', 'jolly', 'just', 'keen', 'keep', 'kill', 'kind', 'kindly', 'king', 'know', 'knowledge', 'labour', 'lady', 'lamp', 'land', 'language', 'laptop', 'large', 'late', 'laugh', 'launch', 'law', 'lay', 'lazy', 'lead', 'leader', 'lean', 'learn', 'leave', 'left', 'leg', 'lengthy', 'let', 'level', 'lie', 'life', 'lift', 'light', 'like', 'likely', 'limit', 'line', 'link', 'listen', 'live', 'lively', 'lonely', 'long', 'look', 'lord', 'lose', 'loud', 'love', 'lovely', 'low', 'lucky', 'lush', 'machine', 'mad', 'maintain', 'make', 'man', 'manage', 'management', 'manager', 'mark', 'market', 'marry', 'material', 'mature', 'mean', 'measure', 'mechanic', 'medicine', 'meet', 'meeting', 'mention', 'mere', 'merry', 'messy', 'method', 'mid', 'mighty', 'mild', 'mile', 'milliard', 'million', 'mind', 'minister', 'minute', 'miss', 'model', 'modest', 'moist', 'moment', 'monday', 'money', 'month', 'morning', 'mother', 'move', 'movement', 'muddy', 'music', 'musician', 'name', 'narrow', 'nasty', 'nature', 'naughty', 'near', 'neat', 'need', 'negligent', 'new', 'nice', 'night', 'nine', 'nineteen', 'noisy', 'nose', 'note', 'notice', 'number', 'nurse', 'obscure', 'observe', 'obtain', 'occur', 'offer', 'office', 'officer', 'old', 'one', 'open', 'operate', 'operation', 'orange', 'order', 'organisation', 'oval', 'overnight', 'own', 'page', 'pain', 'pale', 'paper', 'parent', 'park', 'party', 'pass', 'patient', 'pay', 'pen', 'pencil', 'people', 'perform', 'performance', 'period', 'person', 'perverse', 'petty', 'pick', 'picture', 'pill', 'pink', 'place', 'plain', 'plan', 'plant', 'play', 'player', 'pleasant', 'point', 'pointed', 'police', 'police officer', 'policy', 'polite', 'poor', 'population', 'posh', 'position', 'power', 'practice', 'prefer', 'prepare', 'present', 'president', 'press', 'pretty', 'prevent', 'price', 'principle', 'problem', 'procedure', 'process', 'produce', 'product', 'production', 'profit', 'profound', 'programme', 'project', 'promise', 'promote', 'prompt', 'property', 'proposal', 'propose', 'protect', 'proud', 'prove', 'provide', 'prudent', 'publish', 'pull', 'pure', 'purple', 'purpose', 'push', 'put', 'quality', 'question', 'quick', 'quiet', 'radio', 'rain', 'raise', 'range', 'rare', 'rate', 'raw', 'reach', 'read', 'ready', 'real', 'realise', 'rear', 'receive', 'recognise', 'record', 'rectangular', 'red', 'reduce', 'refer', 'reflect', 'refuse', 'regard', 'region', 'reject', 'relate', 'relationship', 'release', 'remain', 'remember', 'remote', 'remove', 'repeat', 'replace', 'reply', 'report', 'represent', 'require', 'research', 'resource', 'respect', 'respond', 'responsibility', 'rest', 'result', 'retain', 'retired', 'return', 'reveal', 'rich', 'right', 'ring', 'ripe', 'rise', 'risky', 'river', 'road', 'robust', 'rocky', 'role', 'roof', 'room', 'rough', 'round', 'rude', 'rule', 'run', 'rusty', 'sad', 'safe', 'sales assistant', 'saturday', 'save', 'say', 'scarce', 'scheme', 'school', 'science', 'sea', 'season', 'secretary', 'section', 'sector', 'secure', 'security', 'see', 'seek', 'seem', 'sell', 'send', 'serve', 'service', 'set', 'settle', 'seven', 'seventeen', 'severe', 'sexy', 'shabby', 'shadowy', 'shake', 'shaky', 'shallow', 'shapeless', 'share', 'sheer', 'shiny', 'shoe', 'shoot', 'short', 'show', 'shrewd', 'shy', 'sick', 'side', 'sign', 'silly', 'silver', 'simple', 'sincere', 'sing', 'sit', 'situation', 'six', 'sixteen', 'sky', 'sleep', 'sleepy', 'slight', 'slim', 'slow', 'small', 'smart', 'smile', 'smooth', 'society', 'sofa', 'soft', 'sole', 'son', 'sore', 'sorry', 'sound', 'south', 'spare', 'sparse', 'speak', 'speedy', 'spend', 'split', 'spring', 'square', 'staff', 'stage', 'stale', 'stand', 'standard', 'stare', 'start', 'state', 'stately', 'statement', 'station', 'stay', 'steady', 'sticky', 'stiff', 'still', 'stone', 'stop', 'stormy', 'story', 'stout', 'straight', 'strange', 'street', 'strict', 'strike', 'strong', 'structure', 'student', 'study', 'sturdy', 'subject', 'success', 'suffer', 'suggest', 'suitcase', 'summer', 'sun', 'sunday', 'sunny', 'supply', 'support', 'suppose', 'sure', 'survive', 'swift', 'system', 'table', 'take', 'talk', 'tall', 'tasty', 'taut', 'tax', 'teach', 'teacher', 'team', 'technology', 'tell', 'ten', 'tend', 'term', 'test', 'thank', 'that', 'theory', 'thick', 'thin', 'thing', 'think', 'thirsty', 'thirteen', 'thousand', 'threaten', 'three', 'throw', 'thursday', 'tidy', 'tight', 'time', 'tiny', 'touch', 'tough', 'town', 'trade', 'training', 'travel', 'treat', 'tree', 'triangular', 'tricky', 'true', 'try', 'tuesday', 'turn', 'tv', 'twelve', 'twenty', 'two', 'type', 'ugly', 'understand', 'unfair', 'unhappy', 'union', 'unit', 'united', 'university', 'unlikely', 'unlucky', 'unpleasant', 'untidy', 'urban', 'urgent', 'use', 'vain', 'value', 'vary', 'vast', 'village', 'visit', 'voice', 'void', 'wait', 'walk', 'wall', 'want', 'war', 'warm', 'warn', 'wary', 'watch', 'water', 'way', 'weak', 'wealthy', 'wear', 'weary', 'wednesday', 'week', 'welcome', 'well', 'wet', 'white', 'wide', 'wife', 'wild', 'win', 'window', 'windy', 'winter', 'wise', 'wish', 'witty', 'woman', 'wonder', 'word', 'work', 'work number', 'worker', 'world', 'worry', 'worthy', 'write', 'wrong', 'wry', 'year', 'yellow', 'young', 'zero']
a="abcdefghijklmnopqrstuvwxyz "

s=input()

# Перебираем все возможные ключи
for a1 in range(1,27):
    for b1 in range(27):
        for a2 in range(1,27):
            for b2 in range(27):
                x=r(s,[a1,b1],[a2,b2]) 
                
                if x!=0: # если такой ключ возможен
                    if x.count(' ')/len(x)>0.15: # если частота, с которой встречается
                        #                       пробел, больше определенной
                        f=False
                        for i in (m):    # проверяем входит ли какое-нибудь слово в предполагаемый ответ
                            if i in x:
                                f=True
                                break
                        if f:
                            print(x)
