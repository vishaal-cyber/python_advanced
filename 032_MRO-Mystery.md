# Python Inheritance & MRO Insights

This document analyzes a hierarchy of Python classes demonstrating **single inheritance, multiple inheritance, and cooperative inheritance**.  

The focus is on:
- Class hierarchy (static view)  
- Constructor call order via `super()` (dynamic view, following Python MRO)

---

## 📌 Class Hierarchy

```mermaid
classDiagram
    class Parent
    class Child
    class GrandChild
    class OtherParent
    class MultipleChild
    class Sibling
    class Cousin
    class CoopParent
    class CoopChild1
    class CoopChild2
    class CoopGrandchild

    Parent <|-- Child
    Child <|-- GrandChild

    OtherParent <|-- Sibling

    OtherParent <|-- MultipleChild
    Parent <|-- MultipleChild

    OtherParent <|-- Cousin
    Parent <|-- Cousin

    CoopParent <|-- CoopChild1
    CoopParent <|-- CoopChild2
    CoopChild1 <|-- CoopGrandchild
    CoopChild2 <|-- CoopGrandchild
```

---

## 📌 Constructor Call Order (via `super()`)

### 1. `GrandChild()`

```mermaid
sequenceDiagram
    participant GC as GrandChild
    participant C as Child
    participant P as Parent

    GC->>C: __init__()
    C->>P: __init__()
    P-->>C: prints "Parent class"
    C-->>GC: prints "Child class"
    GC-->>Main: prints "Grandchild class"
```

**Order**: `Parent → Child → GrandChild`

---

### 2. `MultipleChild()`

MRO = `[MultipleChild, OtherParent, Parent, object]`

```mermaid
sequenceDiagram
    participant MC as MultipleChild
    participant OP as OtherParent
    participant P as Parent

    MC->>OP: __init__()
    OP-->>P: super(OtherParent,self).__init__()
    P-->>MC: prints "Parent class"
    OP-->>MC: prints "Other Parent class"
    MC-->>Main: prints "Multiple Child class"
```

**Order**: `OtherParent → Parent → MultipleChild`  
(due to explicit `super(OtherParent, self)` usage)

---

### 3. `Sibling()`

```mermaid
sequenceDiagram
    participant S as Sibling
    participant OP as OtherParent

    S->>OP: __init__()
    OP-->>S: prints "Other Parent class"
    S-->>Main: prints "Sibling class"
```

**Order**: `OtherParent → Sibling`

---

### 4. `Cousin()`

MRO = `[Cousin, OtherParent, Parent, object]`

```mermaid
sequenceDiagram
    participant C as Cousin
    participant P as Parent
    participant OP as OtherParent

    C->>P: __init__() via super(Parent,self)
    P-->>OP: super().__init__()
    OP-->>C: prints "Other Parent class"
    P-->>C: prints "Parent class"
    C-->>Main: prints "Cousin class"
```

**Order**: `OtherParent → Parent → Cousin`

---

### 5. `CoopGrandchild()`

MRO = `[CoopGrandchild, CoopChild1, CoopChild2, CoopParent, object]`

```mermaid
sequenceDiagram
    participant CG as CoopGrandchild
    participant C1 as CoopChild1
    participant C2 as CoopChild2
    participant CP as CoopParent

    CG->>C1: __init__()
    C1->>C2: super().__init__()
    C2->>CP: super().__init__()
    CP-->>C2: prints "Coop Parent class"
    C2-->>C1: prints "Coop Child 2 class"
    C1-->>CG: prints "Coop Child 1 class"
    CG-->>Main: prints "Coop Grandchild class"
```

**Order**: `CoopParent → CoopChild2 → CoopChild1 → CoopGrandchild`  

---

## 🔑 Key Insights
1. **Single inheritance** follows a straight chain (`GrandChild → Child → Parent`).  
2. **Multiple inheritance** depends on MRO and explicit `super()` usage.  
3. **Cooperative inheritance** with `super()` ensures that each parent constructor runs **exactly once** in a diamond hierarchy.  
4. Python MRO resolves ambiguity by linearizing the class hierarchy.  

---

## 📊 MRO & Constructor Call Summary

| Class            | MRO Order                                               | Constructor Call Sequence                        |
|------------------|--------------------------------------------------------|-------------------------------------------------|
| `GrandChild`     | `[GrandChild, Child, Parent, object]`                  | `Parent → Child → GrandChild`                   |
| `MultipleChild`  | `[MultipleChild, OtherParent, Parent, object]`         | `OtherParent → Parent → MultipleChild`          |
| `Sibling`        | `[Sibling, OtherParent, object]`                       | `OtherParent → Sibling`                         |
| `Cousin`         | `[Cousin, OtherParent, Parent, object]`                | `OtherParent → Parent → Cousin`                 |
| `CoopGrandchild` | `[CoopGrandchild, CoopChild1, CoopChild2, CoopParent, object]` | `CoopParent → CoopChild2 → CoopChild1 → CoopGrandchild` |

---
