from time import sleep, time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}' + '\n')

    sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f'Работа потоков {end_time - start_time}')


start_time_threads = time()
threads = []
write_words_threads = [(10, 'example5.txt'),
(30, 'example6.txt'),
(200, 'example7.txt'),
(100, 'example8.txt')]

for argum in write_words_threads:
    thread = threading.Thread(target=write_words, args=argum)
    threads.append(thread)
    thread.start()
    thread.join()

end_time_threads = time()
print(f'Работа потоков {end_time_threads - start_time_threads}')