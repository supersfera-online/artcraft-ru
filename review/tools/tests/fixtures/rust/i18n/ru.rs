//! Russian fixture: match arms, block arms, tuples, raw strings, comments with "fake" => "strings".
// Russian translation © 2026 SuperSfera LLC, MIT OR Apache-2.0
pub(super) fn translate(text: &str) -> Option<&'static str> {
    Some(match text {
        "Save" => "Сохранить",
        "Open" | "Open…" => "Открыть…",
        "Long {name}" => {
            "Длинный {name}"
        }
        r#"Raw "quoted""# => "Сырой «в кавычках»",
        "Escaped\nline" => "Экранированная строка",
        "Save" => "Дубль",
        _ => return None,
    })
}
