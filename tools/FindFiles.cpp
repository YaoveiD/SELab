#include <dirent.h>
#include <stdio.h>
#include <string.h>

const int P = 1111;
const char *start_dir = "../avro/lang/java";
const char *output_file = "../commits/filelist.txt";
char path_buffer[P];

int str_endswith_java(const char *s) {
  size_t slen = strlen(s);
  static const char *suff = ".java";
  static size_t sufflen = strlen(suff);
  return slen >= sufflen && !memcmp(s + slen - sufflen, suff, sufflen);
}

void recurse(const char *dir_name) {
  DIR *d;
  struct dirent *dir;
  d = opendir(dir_name);

  if (d) {
    while ((dir = readdir(d)) != NULL) {
      if (dir->d_type == DT_REG) {
        if (str_endswith_java(dir->d_name))
          printf("%s/%s\n", path_buffer + 8, dir->d_name);
      } else if (dir->d_type == DT_DIR &&
                 strcmp(dir->d_name, "..") && strcmp(dir->d_name, ".")) {
        size_t n = strlen(path_buffer);
        path_buffer[n] = '/';
        path_buffer[n + 1] = 0;
        strcat(path_buffer, dir->d_name);
        recurse(path_buffer);
        n = strlen(path_buffer);
        size_t m = strlen(dir->d_name);
        path_buffer[n - m - 1] = 0;
      }
    }

    closedir(d);
  }
}

int main() {
  freopen(output_file, "w", stdout);
  strcat(path_buffer, start_dir);
  recurse(start_dir);
}