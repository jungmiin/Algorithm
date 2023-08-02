def music_to_array(music, time):
    sound = []
    i = 0
    sec = 0
    while True:
        if time == sec:
            break
        if i%len(music) < len(music)-1 and music[i%len(music)+1] == '#':
            sound.append(music[i%len(music):i%len(music)+2])
            i += 2
        else:
            sound.append(music[i%len(music)])
            i += 1
        sec += 1
    return sound

def solution(m, musicinfos):
    answer = ''
    answer_time = 0
    infos = []
    m_array = music_to_array(m, len(m)-m.count('#'))
    
    for musicinfo in musicinfos:
        tmp = []
        [start, end, title, music] = musicinfo.split(',')
        [start_min, start_sec] = start.split(':')
        [end_min, end_sec] = end.split(':')
        time = (int(end_min)-int(start_min))*60 + int(end_sec)-int(start_sec)
        hash_count = music.count('#')
        sound = music_to_array(music, time)
        infos.append([time, title, sound])
    
    for [time, title, sound] in infos:
        print(','.join(m_array)+',',','.join(sound)+',')
        if ','.join(m_array)+',' in ','.join(sound)+',':
            
            if answer != '':
                if time > answer_time:
                    answer = title
                    answer_time = time
            else:
                answer = title
                answer_time = time
    
        # for i in range(len(sound)-len(m_array)+1):
        #     if m_array == sound[i:i+len(m_array)]:
        #         if answer != '':
        #             if time > answer_time:
        #                 answer = title
        #                 answer_time = time
        #         else:
        #             answer = title
        #             answer_time = time
    
    return '(None)' if answer == '' else answer