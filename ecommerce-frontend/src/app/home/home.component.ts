import { Component, OnInit } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MatSnackBar} from '@angular/material/snack-bar';

interface Product {
  product: string;
  subcategory: string;
  category: string;
  editMode?: boolean;
}
interface Category {
  name: string;
  id: number;
}
interface SubCategory{
  name: string;
  category: number;
  id: number;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})


export class HomeComponent implements OnInit {

  displayedColumns: string[] = ['product', 'subcategory', 'category'];
  dataSource: MatTableDataSource<Product>;
  categories: Category[];
  subcategories: SubCategory[];
  selectedCategory: number;
  selectedSubcategory: number;
  productName: string;
  showAction: boolean= false;

  @ViewChild(MatSort, { static: true }) sort: MatSort;

  constructor(private httpClient: HttpClient, private _snackBar: MatSnackBar) {
   
  }

  cancel() {
    if (!this.showAction){
      return
    }
    this.showAction = false;
    this.dataSource.data.pop();
    this.dataSource._updateChangeSubscription();
  }

  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action, {
      duration: 4000,
    });
  }
  getProductDetails() {
    this.httpClient.get("http://127.0.0.1:8000/products/").toPromise().then((data: Product[]) => {
      this.dataSource = new MatTableDataSource(data);
      this.dataSource.sort = this.sort;
    })
  }

  getCategoyDetails() {
    this.httpClient.get("http://127.0.0.1:8000/categories").toPromise().then((data: Category[]) => {
      this.categories = data
    })
  }

  getSubcategoyDetails() {
    this.httpClient.get("http://127.0.0.1:8000/subcategories/").toPromise().then((data: SubCategory[]) => {
      this.subcategories = data
    })
  }

  onOptionsSelectedSubcategory(event) {
    const value = event.target.value
    this.selectedSubcategory = value;
  }

  onOptionsSelectedCategory(event) {

    const value = event.target.value
    this.selectedCategory = value;
  }

  saveProductDetail() {
    console.log(this.selectedSubcategory);
    console.log(this.selectedCategory);
    let proceed: boolean =false;
    this.subcategories.forEach(subcategory => {
      if (subcategory.id == Number(this.selectedSubcategory) && subcategory.category == Number(this.selectedCategory))
      {
        proceed= true;
      }
    })
    if (!proceed){
      this.openSnackBar("Wrong mapping for Category and SubCategory", "Error")
    }else{
      
      this.httpClient.post("http://127.0.0.1:8000/products/", 
        {
          name: this.productName,
          subcategory: this.selectedSubcategory
        }
      ).toPromise().then((data: any) => {
        this.getProductDetails();
        this.showAction =false;
        this.openSnackBar("Product added successfully", "Success")
      })
    }
  }

  newRow() {
    if (this.showAction){
      return
    }
    this.dataSource.data.push({
      category: "",
      subcategory: "",
      product:"",
      editMode: true
    });
    this.dataSource._updateChangeSubscription();
    this.showAction=true
  }

  ngOnInit() {
    this.getProductDetails();
    this.getCategoyDetails();
    this.getSubcategoyDetails();
  }

}