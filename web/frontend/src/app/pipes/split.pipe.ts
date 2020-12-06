import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'split'
})
export class SplitPipe implements PipeTransform {

  transform(text: string, by: string, index: number = 1) {
    let arr = text.split(by); // split text by "by" parameter
    if (index === -1) {
      index = arr.length - 1
    }
    return arr[index] // after splitting to array return wanted index
  }
}