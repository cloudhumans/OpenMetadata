/*
 *  Copyright 2021 Collate
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

import { HTMLAttributes } from 'react';

export interface Filter {
  key: string;
  value: string;
}
export interface AdvanceSearchProp extends HTMLAttributes<HTMLDivElement> {
  searchValue: string;
  isTourRoute?: boolean;
  pathname: string;
  isSearchBoxOpen: boolean;
  handleSearchChange: (value: string) => void;
  handleOnClick: () => void;
  handleKeyDown: (e: React.KeyboardEvent<HTMLInputElement>) => void;
  handleSearchBoxOpen: (value: boolean) => void;
  onFilterChange: (filters: Array<Filter>) => void;
}
