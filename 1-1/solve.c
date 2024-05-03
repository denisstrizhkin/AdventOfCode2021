#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

int main(void) {
  FILE* fp = fopen("input", "r");
  if (!fp) {
    fprintf(stderr, "can't open file: %s\n", strerror(errno));
    return EXIT_FAILURE;
  }

  char *line = NULL;
  size_t len = 0;
    
  if (getline(&line, &len, fp) == -1) {
    free(line);
    fprintf(stderr, "failed to read line: %s\n", strerror(errno));
    return EXIT_FAILURE;
  }

  char *endptr;
  int32_t previous = strtol(line, &endptr, 10);
    
  int32_t total = 0;
  while (getline(&line, &len, fp) != -1) {
    int32_t current = strtol(line, &endptr, 10);
    if (current > previous) {
      total++;
    }
    previous = current;
  }

  printf("answer: %" PRId32 "\n", total);
  free(line);
  fclose(fp);
  
  fp = fopen("answer", "w");
  if (!fp) {
    fprintf(stderr, "can't open file: %s\n", strerror(errno));
    return EXIT_FAILURE;
  }

  fprintf(fp, "%" PRId32 "\n", total);
  fclose(fp);
  
  return EXIT_SUCCESS;
}
